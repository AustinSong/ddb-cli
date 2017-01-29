import click

import config

import pydocumentdb.document_client as document_client

# Creates the DocumentDB client connection.
@click.group()
@click.pass_context
def main(ctx):
    click.echo("Creating client")
    ctx.obj = document_client.DocumentClient(config.DDB_HOST,
                                             {'masterKey':config.DDB_KEY})

# Creates a database with the name as the id.  Utilizes the client from
# main function.
@main.command()
@click.argument('name')
@click.pass_obj
def createdb(ctx, name):
    click.echo("Connecting to DocumentDB")
    client = ctx
    click.echo("Client created")
    db = client.CreateDatabase({'id':name})
    click.echo('Created db with name: ' + name)

if __name__=='__main__':
    main()
