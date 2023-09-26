# Project Creator

Project Creator is a Python command-line tool designed to streamline the process of setting up a new Python project. It simplifies the creation of project directories, Conda environments, Git repositories, and even offers GitHub integration. Whether you're starting a new personal project or collaborating with a team, Project Creator can save you valuable time and ensure that your project is set up correctly from the beginning.

## Table of Contents

- [Why Use Project Creator?](#why-use-project-creator)
- [Features](#features)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Why Use Project Creator?

Starting a new software project often involves a series of manual tasks, such as creating directories, setting up a Conda environment, initializing a Git repository, and linking it to a GitHub repository. These tasks can be time-consuming and error-prone. Project Creator automates these processes, providing the following benefits:

- **Efficiency**: Project Creator allows you to set up a project with just a few simple commands. It automates repetitive tasks, enabling you to start coding faster.

- **Consistency**: Project Creator enforces a standardized project structure, reducing the chances of overlooking essential files or directories.

- **Git Integration**: Project Creator automatically initializes a Git repository, making your project version-controlled from the start. It even offers GitHub integration, creating a GitHub repository and linking it to your local repository if desired.

- **Customization**: While offering automation, Project Creator is flexible. You can customize your project's Python version, directory structure, and more.

## Features

- **Conda Environment Creation**: Easily create a Conda environment with your specified Python version for your project.

- **Standard Project Structure**: Project Creator sets up a standard project structure with essential directories and files.

- **Git Integration**: Initialize a Git repository, make an initial commit, and even create a GitHub repository with ease.

- **GitHub Integration**: Optionally create a new GitHub repository for your project, link your local repository to it, and push your code to GitHub.

## Usage

To create a new project, run the `main.py` script with the following command:

```bash
python main.py <project_name> <python_version>
```

## Project Structure
Your project structure will look like this:

    CompanyName/
    └── MyProject/
        ├── .git/
        │   ├── hooks/
        │   ├── info/
        │   ├── logs/
        │   ├── objects/
        ├── .env
        ├── .gitignore
        ├── README.md
        ├── requirements.txt
        └── main.py

**.git/**: The Git repository for version control.

**.env**: Add your environment variables here.

**.gitignore**: A Git ignore file to specify which files and directories should be ignored by Git.

**README.md**: A README file for your project documentation.

**requirements.txt**: Add your project dependencies here.

**main.py**: The main script to create a new project.

## Getting Started
Clone this repository to your local machine.

- Customize the `main.py` script by replacing `"your_github_token_here"` with your actual GitHub Personal Access Token (this is optional).

- Run the `main.py` script to create a new project. Follow the on-screen prompts.

- Activate your Conda environment using the following command:

```bash
conda activate <project_name>
```

Start working on your project!


## Contributing
Contributions are welcome! If you have any ideas or improvements to suggest, please create an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
