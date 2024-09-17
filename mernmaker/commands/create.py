import click
from mernmaker.utils.server_setup import server_setup
from mernmaker.utils.client_setup import client_setup
from mernmaker.utils.helpers import other_setups
from mernmaker.utils.lint_setup import lint_setup
import subprocess
import sys

@click.command()
@click.argument('app_name')
@click.option('--tailwind', prompt='Do you want to use Tailwind CSS?', help='Whether to use Tailwind CSS or not')
@click.option('--lint', prompt='Do you want to use ESLint?', help='Whether to use ESLint or not')
def create(app_name, tailwind, lint):
    server_setup(app_name)
    client_setup(app_name, tailwind)
    other_setups(app_name)

    if sys.platform == 'win32':
        subprocess.run(["npm.cmd", "install", "express", "mongoose", "dotenv"], cwd=f'{app_name}', shell=True)
        subprocess.run(["npm.cmd", "install", "nodemon", "--save-dev"], cwd=f'{app_name}', shell=True)
        subprocess.run(["npm.cmd", "run", "setup"], cwd=f'{app_name}', shell=True)
    else:
        subprocess.run(["npm", "install", "express", "mongoose", "dotenv"], cwd=f'{app_name}')
        subprocess.run(["npm", "install", "nodemon", "--save-dev"], cwd=f'{app_name}')
        subprocess.run(["npm", "run", "setup"], cwd=f'{app_name}')

    if lint == 'yes':
        lint_setup(app_name)

    click.echo("\n\n\n\n\n")
    click.echo(f"Created MERN app, {app_name}. Now run,\n")
    click.echo(f"       cd {app_name}\n")
    click.echo("Edit .env file with your MongoDB URI\n")
    click.echo("        mernmaker changelog update\n")
    click.echo("        mernmaker lint\n\n")
