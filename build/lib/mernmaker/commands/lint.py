import os
import click
import subprocess
from mernmaker.utils.lint_setup import lint_setup

@click.command()
@click.argument('app_name', default='.')
def lint(app_name):
    """Run ESLint on the specified app."""
    
    eslint_config_path = os.path.join(app_name, 'eslint.config.js')
    
    if not os.path.isfile(eslint_config_path):
        click.echo("No ESLint config found.")
        if click.confirm("Would you like to create one?", default=True):
            lint_setup(app_name)  
            click.echo("ESLint config created successfully.")
        else:
            click.echo("Exiting without creating ESLint config.")
            return

    try:
        subprocess.run(["npm", "run", "lint"], cwd=app_name, check=True)
        click.echo("Linting completed successfully.")
    except subprocess.CalledProcessError:
        click.echo("Error: Linting failed.")
