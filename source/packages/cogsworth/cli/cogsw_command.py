#!/usr/bin/env python3
"""
.. module:: cogsw_command
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: The script entrypoint for the 'cogsw' command.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import click

from cogsworth.cli.cmdtree.datastore import group_cogsw_datastore


@click.group("cogsw")
@click.option('-v', '--verbose', count=True)
@click.pass_context
def cogsw_root_command(ctx, verbose):

    if verbose == 0:
        ctx.interactive = True
    else:
        ctx.interactive = False

        ctx.log_level_console = "WARN"
        if verbose == 1:
            ctx.log_level_console = "INFO"
        elif verbose == 2:
            ctx.log_level_console = "DEBUG"
        elif verbose > 2:
            ctx.log_level_console = "NOTSET"

    return

cogsw_root_command.add_command(group_cogsw_datastore)

if __name__ == '__main__':
    cogsw_root_command()