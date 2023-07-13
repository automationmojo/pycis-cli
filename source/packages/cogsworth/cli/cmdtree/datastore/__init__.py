__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import click

from cogsworth.cli.cmdtree.datastore.couchdb import group_cogsw_datastore_couchdb
from cogsworth.cli.cmdtree.datastore.mongodb import group_cogsw_datastore_mongodb

datastore_HELP = "Contains commands groups for datastore test results to different types of data stores."

@click.group("datastore", help=datastore_HELP)
def group_cogsw_datastore():
    return

group_cogsw_datastore.add_command(group_cogsw_datastore_couchdb)
group_cogsw_datastore.add_command(group_cogsw_datastore_mongodb)
