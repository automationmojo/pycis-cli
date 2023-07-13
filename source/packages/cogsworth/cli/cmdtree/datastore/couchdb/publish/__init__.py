
__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import click

from cogsworth.cli.cmdtree.datastore.couchdb.publish.testrun import command_datastore_couchdb_publish_testrun


@click.group("couchdb", help="Contains commands datastore test results to CouchDB.")
def group_cogsw_datastore_couchdb_publish():
    return

group_cogsw_datastore_couchdb_publish.add_command(command_datastore_couchdb_publish_testrun)