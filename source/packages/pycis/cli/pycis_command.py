#!/usr/bin/env python3
"""
.. module:: pycis_command
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: The script entrypoint for the 'pycis' command.

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


@click.group("pycis")
@click.option('-v', '--verbose', count=True)
@click.pass_context
def pycis_root_command(ctx, verbose):

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


from pycis.cli.cmdtree import add_groups_and_commands

add_groups_and_commands(pycis_root_command)


if __name__ == '__main__':
    pycis_root_command()