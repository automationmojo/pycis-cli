
__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import click


@click.group("tracking", help="Contains commands for interoperating with tracking software and services.")
def group_pycis_tracking():
    return


def add_groups_and_commands(parent: click.Group):

    from pycis.cli.cmdtree.tracking.jira import add_groups_and_commands as jira_add_groups_and_commands

    jira_add_groups_and_commands(group_pycis_tracking)

    parent.add_command(group_pycis_tracking)

    return