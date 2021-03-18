import click

@click.command()
@click.option('--name', help='Person to greet.'
)
def hello(name=None):
    if name is not None:
        click.echo('hello {}'.format(name))
    else:
        click.echo('hello world')
