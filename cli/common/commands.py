# Copyright 2017 Red Hat, Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import click


@click.command()
@click.option("--server", is_flag=True, help="Server version.")
@click.pass_obj
def version(app_context, server):
    """Display the current version."""
    if server:
        click.echo("Transtats server 0.1.3")
    click.echo("Transtats client %s" % app_context.version)
