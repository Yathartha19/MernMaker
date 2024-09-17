# MernMaker

**MernMaker** is a command-line interface (CLI) tool designed to streamline the process of building and managing MERN stack applications. This tool provides developers with an intuitive interface to quickly scaffold projects, manage dependencies, and automate common development tasks.

### Getting Started

To get started with **MernMaker**, 
  Download the files, and run (in the folder with setup.py)

      pip install click
      pip install --user . 

  Add to PATH if not done. (see below for guide)

  Now to create a new MERN app,
  
      mernmaker create your_app_name

  To edit or view github changelog,

      mernmaker changelog update
      mernmaker changelog view

  To view code stats,

      mernmaker stats

  Linting,

      mernmaker lint


#####dding to PATH

Make sure that the npm executable is included in your system's PATH. You can do this by following these steps:
Right-click on "This PC" or "My Computer" and select "Properties."
Click on "Advanced system settings" and then click on the "Environment Variables" button.
In the "System variables" section, scroll down and find the Path variable. Select it and click "Edit."
Ensure that the path to your Node.js installation (e.g., C:\Program Files\nodejs\) is listed. If not, add it.
Restart your terminal or command prompt:

After making changes to the PATH variable, restart your command prompt to apply the changes.

### Default Configuration
  MongoDB with choice for Tailwind CSS or pure CSS, ExpressJS and ReactJS.
  To change these you will have to edit the main.py file.

### Key Features

- **Project Scaffolding**: Easily create new MERN stack projects with predefined templates, saving time on setup.
- **Dependency Management**: Automatically install and manage essential packages for your MERN applications.
- **Custom Scripts**: Run custom scripts and commands tailored to your development workflow.
- **User-Friendly Interface**: Simple and intuitive CLI for both beginners and experienced developers.
