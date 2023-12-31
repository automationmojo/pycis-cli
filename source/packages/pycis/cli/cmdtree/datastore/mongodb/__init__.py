
__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import click

from pycis.cli.cmdtree.datastore.mongodb.publish import command_pycis_datastore_mongodb_publish


@click.group("mongodb", help="Contains commands datastore test results to MongoDB.")
def group_pycis_datastore_mongodb():
    return

group_pycis_datastore_mongodb.add_command(command_pycis_datastore_mongodb_publish)
