import click
import subprocess
from datetime import datetime
import os

@click.command()
@click.argument('parg')
def changelog(parg):
    if parg == 'update':
        cur_work_dir = os.getcwd()
        changelog_path = os.path.join(cur_work_dir, 'CHANGELOG.md')

        if not os.path.exists(changelog_path):
            with open(changelog_path, 'w') as changelog_file:
                changelog_file.write("# Changelog\n\n")

        try:
            commits = subprocess.check_output(
                ["git", "log", "--pretty=format:%h - %s (%an)", "--no-merges", "-n", "5"], 
                text=True
            ).strip()
        except subprocess.CalledProcessError as e:
            click.echo("Error fetching commits. Please ensure you're in a Git repository.")
            return

        if not commits:
            click.echo("No new commits found.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d")
        with open(changelog_path, 'a') as changelog_file:
            changelog_file.write(f"## {timestamp}\n")
            changelog_file.write(f"{commits}\n\n")

        click.echo(f"Changelog updated with latest commits:\n{commits}")
    
    elif parg == 'view':
        cur_work_dir = os.getcwd()
        changelog_path = os.path.join(cur_work_dir, 'CHANGELOG.md')
        
        if os.path.exists(changelog_path):
            with open(changelog_path, 'r') as changelog_file:
                click.echo(click.style(changelog_file.read(), fg='green'))
        else:
            click.echo("Changelog file not found.")
