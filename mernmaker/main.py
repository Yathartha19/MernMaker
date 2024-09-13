import os
import click
import subprocess

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

    subprocess.run(["npm", "init", "-y"], cwd=f'{app_name}')

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

def frontend_setup(app_name):

    os.makedirs(f'{app_name}/frontend', exist_ok=True)

    subprocess.run(["npm", "create", "vite@latest", "frontend", "--", "--template", "react"], cwd=app_name) 

    click.echo(f'\n\n\n\n\n\n\n\n\n\n\n Please wait...')

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

@click.command()
@click.option('--app_name', prompt='Enter the name of your MERN app', help='The name of the MERN app to create')
def main(app_name):

    server_setup(app_name)
    frontend_setup(app_name)
    other_setups(app_name)

    subprocess.run(["npm", "install", "express", "mongoose", "dotenv"], cwd=f'{app_name}')
    subprocess.run(["npm", "install", "nodemon", "--save-dev"], cwd=f'{app_name}')
    subprocess.run(["npm", "run", "setup"], cwd=f'{app_name}')

    click.echo("\n\n\n\n\n\n")
    click.echo(f"Created MERN app, {app_name}. Now run,\n")
    click.echo(f"       cd {app_name}\n")
    click.echo("Edit .env file with your MongoDB URI\n\n")

if __name__ == '__main__':
    main()
