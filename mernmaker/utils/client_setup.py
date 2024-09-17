import os
import subprocess
import sys

def client_setup(app_name, tailwind):
    os.makedirs(f'{app_name}/frontend', exist_ok=True)
    if sys.platform == 'win32':
        subprocess.run(["npm.cmd", "create", "vite@latest", "frontend", "--", "--template", "react"], cwd=app_name, shell=True)
    else:
        subprocess.run(["npm", "create", "vite@latest", "frontend", "--", "--template", "react"], cwd=app_name)

    if tailwind.lower() == 'yes' or tailwind.lower() == 'y':
        frontend_dir = os.path.join(app_name, 'frontend')
        if sys.platform == 'win32':
            subprocess.run(["npm.cmd", "install", "-D", "tailwindcss", "postcss", "autoprefixer"], cwd=frontend_dir, shell=True)
        else:
            subprocess.run(["npm", "install", "-D", "tailwindcss", "postcss", "autoprefixer"], cwd=frontend_dir)

        if sys.platform == 'win32':
            subprocess.run(["npx.cmd", "tailwindcss", "init", "-p"], cwd=frontend_dir, shell=True)
        else:
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
