import click

import config

import pydocumentdb.document_client as document_client

@click.group()
@click.option('--host', help='Host')
@click.option('--key', help='Key')
@click.pass_context
def main(ctx, host, key):
    ctx.obj = document_client.DocumentClient(host, {'masterKey':key})

@main.command()
@click.argument('name')
@click.pass_obj
def createdb(ctx, name):
    client = ctx    
    db = client.CreateDatabase({'id':name})
    click.echo('created db with name: ' + name)

if __name__=='__main__':
    main()
