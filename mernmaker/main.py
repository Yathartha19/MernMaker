import os
import click
import subprocess
from datetime import datetime

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')

def copy_template(src, dst):
    try:
        print(f"Trying to open template: {src}") 
        with open(src, 'r') as template_file:
            content = template_file.read()
        
        with open(dst, 'w') as dst_file:
            dst_file.write(content)
    except FileNotFoundError:
        print(f"Error: The template file {src} does not exist.")
        raise

def server_setup(app_name):

    os.makedirs(app_name)
    os.makedirs(f'{app_name}/backend', exist_ok=True)

    subprocess.run(["npm", "init", "-y"], cwd=f'{app_name}', shell=True)

    package_json_template = os.path.join(TEMPLATES_DIR, 'package.json')
    db_js_template = os.path.join(TEMPLATES_DIR, 'db.js')
    server_js_template = os.path.join(TEMPLATES_DIR, 'server.js')

    copy_template(package_json_template, f'{app_name}/package.json')
    
    os.makedirs(f'{app_name}/backend/config', exist_ok=True)
    copy_template(db_js_template, f'{app_name}/backend/config/db.js')
    
    copy_template(server_js_template, f'{app_name}/backend/server.js')

    os.makedirs(f'{app_name}/backend/models', exist_ok=True)
    os.makedirs(f'{app_name}/backend/routes', exist_ok=True)
    os.makedirs(f'{app_name}/backend/controllers', exist_ok=True)

    print(f'Created server for {app_name}')

def frontend_setup(app_name, tailwind):

    os.makedirs(f'{app_name}/frontend', exist_ok=True)

    subprocess.run(["npm", "create", "vite@latest", "frontend", "--", "--template", "react"], cwd=app_name) 

    click.echo(f'\n\n\n\n\n\n\n\n\n\n\n Please wait...')

    if tailwind.lower() == 'yes' or tailwind.lower() == 'y':
        frontend_dir = os.path.join(app_name, 'frontend')
        
        subprocess.run(["npm", "install", "-D", "tailwindcss", "postcss", "autoprefixer"], cwd=frontend_dir)
        subprocess.run(["npx", "tailwindcss", "init", "-p"], cwd=frontend_dir)

        with open(os.path.join(frontend_dir, 'src', 'index.css'), 'a') as css_file:
            css_file.write("\n@tailwind base;\n@tailwind components;\n@tailwind utilities;\n")

        tailwind_config_path = os.path.join(frontend_dir, 'tailwind.config.js')
        with open(tailwind_config_path, 'r') as tailwind_config_file:
            config_content = tailwind_config_file.read()
        new_config_content = config_content.replace(
            "content: [],",
            "content: [\"./index.html\", \"./src/**/*.{js,jsx,ts,tsx}\"],"
        )
        with open(tailwind_config_path, 'w') as tailwind_config_file:
            tailwind_config_file.write(new_config_content)

def other_setups(app_name):

    with open(os.path.join(app_name, '.env'), 'w') as env_file:
        env_file.write("PORT=5000\nMONGO_URI=<replace_this_with_your_mongodb_uri>") 

    frontend_gitignore_path = os.path.join(app_name, 'frontend', '.gitignore')
    
    if os.path.exists(frontend_gitignore_path):
        with open(frontend_gitignore_path, 'r') as gitignore_file:
            gitignore_contents = gitignore_file.read()

        with open(os.path.join(app_name, '.gitignore'), 'w') as new_gitignore_file:
            new_gitignore_file.write(gitignore_contents)
            new_gitignore_file.write("\n.env\n")

        os.remove(frontend_gitignore_path)

@click.group()
def main():
    pass

@click.command()
@click.argument('app_name')
@click.option('--tailwind', prompt='Do you want to use Tailwind CSS?', help='Whether to use Tailwind CSS or not')
def create(app_name, tailwind):

    server_setup(app_name)
    frontend_setup(app_name, tailwind)
    other_setups(app_name)

    subprocess.run(["npm", "install", "express", "mongoose", "dotenv"], cwd=f'{app_name}')
    subprocess.run(["npm", "install", "nodemon", "--save-dev"], cwd=f'{app_name}')
    subprocess.run(["npm", "run", "setup"], cwd=f'{app_name}')

    click.echo("\n\n\n\n\n\n")
    click.echo(f"Created MERN app, {app_name}. Now run,\n")
    click.echo(f"       cd {app_name}\n")
    click.echo("Edit .env file with your MongoDB URI\n\n")

@click.command()
@click.argument('parg')
def changelog(parg):
    if parg == 'update':
        """Automatically update the changelog with the latest Git commits."""
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
        """Display the changelog."""
        cur_work_dir = os.getcwd()
        changelog_path = os.path.join(cur_work_dir, 'CHANGELOG.md')
        
        if os.path.exists(changelog_path):
            with open(changelog_path, 'r') as changelog_file:
                click.echo(click.style(changelog_file.read(), fg='green'))
        else:
            click.echo("Changelog file not found.")

@click.command()
@click.argument('app_name')
def stats(app_name):
    """Display project statistics for the specified app."""
    
    def count_lines_of_code(directory):
        total_lines = 0
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(('.js', '.jsx', '.ts', '.tsx', '.py')):
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        total_lines += sum(1 for line in f)
        return total_lines


    backend_directory = os.path.join(app_name, 'backend')
    frontend_directory = os.path.join(app_name, 'frontend')

    loc = count_lines_of_code(backend_directory) + count_lines_of_code(frontend_directory)
    click.echo(f'Total Lines of Code: {loc}')

    click.echo('\nTest Coverage:')


main.add_command(create)
main.add_command(changelog)
main.add_command(stats)

if __name__ == '__main__':
    main()
