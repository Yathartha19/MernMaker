import os
import subprocess
from mernmaker.utils.helpers import copy_template

def server_setup(app_name):
    os.makedirs(app_name)
    os.makedirs(f'{app_name}/backend', exist_ok=True)

    subprocess.run(["npm", "init", "-y"], cwd=f'{app_name}', shell=True)

    TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), '..', 'templates')

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
