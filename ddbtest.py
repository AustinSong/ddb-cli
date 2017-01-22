import click

import config

import pydocumentdb.document_client as document_client

@click.command()
@click.argument('name')
def connectdb(name):
    client = document_client.DocumentClient(config.DDB_HOST,
                                            {'masterKey':config.DDB_KEY})
    click.echo(client)
    click.echo('connected to ddb emulator')

if __name__=='__main__':
    connectdb()
