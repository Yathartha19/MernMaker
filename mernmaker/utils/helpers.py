import os

def copy_template(src, dst):
    try:
        with open(src, 'r') as template_file:
            content = template_file.read()
        with open(dst, 'w') as dst_file:
            dst_file.write(content)
    except FileNotFoundError:
        print(f"Error: The template file {src} does not exist.")
        raise

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
