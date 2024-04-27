__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

from typing import List, Union

import os
import sys

from http import HTTPStatus

import click
import requests

from mojo.credentials.apitokencredential import ApiTokenCredential
from mojo.credentials.personalapitokencredential import PersonalApiTokenCredential
from mojo.credentials.basiccredential import BasicCredential

from mojo.xmods.xclick import NORMALIZED_STRING

HELP_JQL = "A Jira Query String that is used to limit the effect Jira tickets."
HELP_LIMIT = "Limit the number of issues that can be modified by the command."
HELP_COMMENT = "A comment to append to the select Jira tickets. (must be specified if '--comment-source' is not passed)"
HELP_COMMENT_SOURCE = "A source path specifying where to get comment contents.  (must be specified if '--comment' is not passed)"
HELP_CREDENTIAL_SOURCE = "The source location of a credential catalog."
HELP_CREDENTIAL = "The name of a Jira credential to use from the specified credential catalog."

@click.command("comment")
@click.option("--jira", "jirahost", required=True, type=NORMALIZED_STRING, help=HELP_JQL)
@click.option("--jql", "jql", required=True, multiple=True, type=NORMALIZED_STRING, help=HELP_JQL)
@click.option("--comment", required=False, type=NORMALIZED_STRING, help=HELP_COMMENT)
@click.option("--comment-source", required=False, type=NORMALIZED_STRING, help=HELP_COMMENT_SOURCE)
@click.option("--credential", required=True, type=NORMALIZED_STRING, help=HELP_CREDENTIAL)
@click.option("--credential-source", required=False, default=None, type=NORMALIZED_STRING, help=HELP_COMMENT_SOURCE)
@click.option("--limit", required=False, default=1, help=HELP_LIMIT)
def command_pycis_tracking_jira_comment(jirahost: str, jql: List[str], comment: Union[str, None], comment_source: Union[str, None], credential: str,
                                        credential_source: Union[str, None], limit: bool):
    
    if comment is None and comment_source is None:
        errmsg = "You must ONLY specify either the 'comment' or 'comment-source' option."
        raise click.BadOptionUsage(errmsg)
    
    if comment is not None and comment_source is not None:
        errmsg = "You must ONLY specify either the 'comment' or 'comment-source' option.  You cannot use both."
        raise click.BadOptionUsage(errmsg)

    if comment_source is not None:
        if comment_source.startswith("http:") or comment_source.startswith("https:"):
            resp = requests.get(comment_source)
            if resp.status_code == HTTPStatus.OK:
                comment = resp.content
            else:
                errmsg_lines = [
                    f"Invalid comment source specified. url={comment_source}",
                    f"STATUS CODE: {resp.status_code}",
                    f"CONTENT:"
                ]
                errmsg_lines.append(resp.content)

                errmsg = os.linesep.join(errmsg_lines)
                
                raise click.BadParameter(errmsg)
        else:
            with open(comment_source, 'r') as cs:
                comment = cs.read()

    from mojo.config.optionoverrides import MOJO_CONFIG_OPTION_OVERRIDES
    from mojo.config.configurationmaps import resolve_configuration_maps

    if credential_source is not None:
        MOJO_CONFIG_OPTION_OVERRIDES.override_config_credentials_files([credential_source])

    resolve_configuration_maps(use_credentials=True, use_landscape=False, use_topology=False, use_runtime=False)

    from mojo.config.wellknown import CredentialManagerSingleton

    credmgr = CredentialManagerSingleton()

    jiracred: Union[ApiTokenCredential, BasicCredential] = credmgr.lookup_credential(credential)

    from jira import JIRA, Issue

    jclient = None
    
    if isinstance(jiracred, BasicCredential):
        jclient = JIRA(jirahost, basic_auth=(jiracred.username, jiracred.password))
    elif isinstance(jiracred, PersonalApiTokenCredential):
        jclient = JIRA(jirahost, basic_auth=(jiracred.username, jiracred.token))
    elif isinstance(jiracred, ApiTokenCredential):
        jclient = JIRA(jirahost, token_auth=jiracred.token)
    else:
        errmsg = f"Un-Supported credential type={type(jiracred)}"
        raise ValueError(errmsg)

    issues_found = jclient.search_issues(jql_str=jql)
    if len(issues_found) > 0:
        if len(issues_found) > limit:
            print(f"The number of issues found exceeded the modify limit. limit={limit} found={len(issues_found)}", file=sys.stderr)
            exit(1)

        issue: Issue
        for issue in issues_found:
            jclient.add_comment(issue, comment)

    else:
        print("No issues found.", file=sys.stderr)
        exit(1)

    return
