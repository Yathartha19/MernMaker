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


## Adding MernMaker to Your PATH

To run MernMaker from any terminal window, you need to add it to your system's `PATH`. Follow the instructions below for your operating system.

### macOS

1. Open your terminal.
2. Edit your shell configuration file. This is typically `~/.bash_profile`, `~/.bashrc`, or `~/.zshrc`, depending on the shell you are using. You can open it with a text editor, for example:
   ```bash
   nano ~/.bash_profile
   ```
3. Add the following line to the end of the file, replacing `/path/to/mernmaker` with the actual path where MernMaker is located:
   ```bash
   export PATH="$PATH:/path/to/mernmaker"
   ```
4. Save the changes and exit the editor (in nano, press `CTRL + X`, then `Y`, and `Enter`).
5. Refresh your terminal session by running:
   ```bash
   source ~/.bash_profile
   ```
6. You can verify that it was added correctly by running:
   ```bash
   echo $PATH
   ```

### Windows

1. Press `Win + R`, type `sysdm.cpl`, and hit `Enter`.
2. In the System Properties window, go to the **Advanced** tab and click on **Environment Variables**.
3. In the Environment Variables window, under the **System variables** section, find and select the `Path` variable, then click **Edit**.
4. In the Edit Environment Variable window, click **New** and add the path to your MernMaker installation (e.g., `C:\path\to\mernmaker`).
5. Click **OK** to close all dialog boxes.
6. To verify that it was added correctly, open a new Command Prompt window and run:
   ```cmd
   echo %PATH%
   ```

After adding MernMaker to your `PATH`, you can run it from any terminal or command prompt window by simply typing `mernmaker`.

### Default Configuration
  MongoDB with choice for Tailwind CSS or pure CSS, ExpressJS and ReactJS.
  To change these you will have to edit the main.py file.

### Key Features

- **Project Scaffolding**: Easily create new MERN stack projects with predefined templates, saving time on setup.
- **Dependency Management**: Automatically install and manage essential packages for your MERN applications.
- **Custom Scripts**: Run custom scripts and commands tailored to your development workflow.
- **User-Friendly Interface**: Simple and intuitive CLI for both beginners and experienced developers.
