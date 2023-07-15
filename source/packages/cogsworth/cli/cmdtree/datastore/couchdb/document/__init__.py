
__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import click

from cogsworth.cli.cmdtree.datastore.couchdb.document.build \
    import command_datastore_couchdb_document_build
from cogsworth.cli.cmdtree.datastore.couchdb.document.testrun \
    import command_datastore_couchdb_document_testrun


@click.group("document", help="Contains commands for writing data to a cogsworth document.")
def group_cogsw_datastore_couchdb_document():
    return

group_cogsw_datastore_couchdb_document.add_command(
    command_datastore_couchdb_document_build
)
group_cogsw_datastore_couchdb_document.add_command(
    command_datastore_couchdb_document_testrun
)