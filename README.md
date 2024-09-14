# MernMaker

**MernMaker** is a command-line interface (CLI) tool designed to streamline the process of building and managing MERN stack applications. This tool provides developers with an intuitive interface to quickly scaffold projects, manage dependencies, and automate common development tasks.

### Getting Started

To get started with **MernMaker**, 
  Download the files, and run (in the folder with setup.py)

      pip install click
      pip install --user . 

  Add to PATH if not done.

  Now to create a new MERN app,
  
      mernmaker create your_app_name

  To edit or view github changelog,

      mernmaker changelog update
      mernmaker changelog view

  To view code stats,

      mernmaker stats

### Default Configuration
  MongoDB with choice for Tailwind CSS or pure CSS, ExpressJS and ReactJS.
  To change these you will have to edit the main.py file.

### Key Features

- **Project Scaffolding**: Easily create new MERN stack projects with predefined templates, saving time on setup.
- **Dependency Management**: Automatically install and manage essential packages for your MERN applications.
- **Custom Scripts**: Run custom scripts and commands tailored to your development workflow.
- **User-Friendly Interface**: Simple and intuitive CLI for both beginners and experienced developers.
