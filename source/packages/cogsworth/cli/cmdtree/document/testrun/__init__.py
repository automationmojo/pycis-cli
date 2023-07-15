
__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import click


from cogsworth.cli.cmdtree.document.testrun.create \
    import command_cogsw_document_testrun_create


@click.group("testrun", help="Contains commands for creating a cogsworth 'testrun' document.")
def group_cogsw_document_testrun():
    return

group_cogsw_document_testrun.add_command(
    command_cogsw_document_testrun_create
)