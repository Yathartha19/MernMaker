import os
import subprocess
import json
import click
import sys

def lint_setup(app_name):
    click.echo("Running linters...")

    try:
        if sys.platform == 'win32':
            subprocess.run(["npm.cmd", "install", "eslint", "--save-dev"], cwd=app_name, check=True, shell=True)
        else:
            subprocess.run(["npm", "install", "eslint", "--save-dev"], cwd=app_name, check=True)
        
        if sys.platform == 'win32':
            subprocess.run(["npx.cmd", "eslint", "--init"], cwd=app_name, check=True, shell=True)
        else:
            subprocess.run(["npx", "eslint", "--init"], cwd=app_name,)

        package_json_path = os.path.join(app_name, 'package.json')
        
        with open(package_json_path, 'r') as f:
            package_json = json.load(f)

        package_json['scripts']['lint'] = 'eslint .'

        with open(package_json_path, 'w') as f:
            json.dump(package_json, f, indent=2)

    except subprocess.CalledProcessError:

        click.echo("Error: ESLint encountered an issue.")
        raise

    click.echo("ESLint setup successfully.")