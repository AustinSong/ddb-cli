import click

import config

import pydocumentdb.document_client as document_client
import pydocumentdb.retry_options as retry_opts
import pydocumentdb.documents as documents

# Creates the DocumentDB client connection.
@click.group()
@click.pass_context
def main(ctx):
    click.echo("Creating client")
    ctx.obj = document_client.DocumentClient(config.DDB_HOST,
                                             {'masterKey':config.DDB_KEY}, createConnectionPolicy())

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

def createConnectionPolicy():
    conn_policy = documents.ConnectionPolicy
    conn_policy.EnableEndpointDiscovery = 0
    conn_policy.PreferredLocations = ['West US']
    conn_policy.RetryOptions =  retry_opts.RetryOptions(3)
    conn_policy.RequestTimeout = 3000
    conn_policy.SSLConfiguration = createSSLConfiguration()
    return conn_policy


def createSSLConfiguration():
    ssl_config = documents.SSLConfiguration()
    ssl_config.SSLCaCerts = config.SSL_CERT
    ssl_config.SSLKeyFile = config.SSL_CERT
    ssl_config.SSLCertFile = config.SSL_CERT
    return ssl_config

if __name__=='__main__':
    main()

