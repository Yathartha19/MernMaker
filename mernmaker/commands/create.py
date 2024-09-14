import click
from utils.server_setup import server_setup
from utils.client_setup import client_setup
from utils.helpers import other_setups
import subprocess

@click.command()
@click.argument('app_name')
@click.option('--tailwind', prompt='Do you want to use Tailwind CSS?', help='Whether to use Tailwind CSS or not')
def create(app_name, tailwind):
    server_setup(app_name)
    client_setup(app_name, tailwind)
    other_setups(app_name)

    subprocess.run(["npm", "install", "express", "mongoose", "dotenv"], cwd=f'{app_name}')
    subprocess.run(["npm", "install", "nodemon", "--save-dev"], cwd=f'{app_name}')
    subprocess.run(["npm", "run", "setup"], cwd=f'{app_name}')

    click.echo("\n\n\n\n\n\n")
    click.echo(f"Created MERN app, {app_name}. Now run,\n")
    click.echo(f"       cd {app_name}\n")
    click.echo("Edit .env file with your MongoDB URI\n\n")
