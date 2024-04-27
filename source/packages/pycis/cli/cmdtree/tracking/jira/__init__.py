
__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import click


@click.group("document", help="Contains commands for interoperating with Jira tracking software and services.")
def group_pycis_tracking_jira():
    return


def add_groups_and_commands(parent: click.Group):

    from pycis.cli.cmdtree.tracking.jira.comment import command_pycis_tracking_jira_comment

    group_pycis_tracking_jira.add_command(command_pycis_tracking_jira_comment)

    parent.add_command(group_pycis_tracking_jira)

    return