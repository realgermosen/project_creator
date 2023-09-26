import os
import subprocess
import logging
import requests
from datetime import datetime, timedelta
from utils import check_existing_env

class ProjectCreator:
    def __init__(self, project_name, python_version, github_token):
        self.project_name = project_name
        self.python_version = python_version
        self.github_token = github_token if github_token != 'your_github_token_here' else os.getenv("GITHUB_TOKEN")
        # Initialize logging
        logging.basicConfig(filename='create_project.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


    def create_directories(self):
        try:
            # Ask for company name
            self.company_name = input("\nEnter the company name: ").strip()
            self.company_dir = os.path.join("projects", self.company_name)
    
            # Create company directory if it doesn't exist
            os.makedirs(self.company_dir, exist_ok=True)
    
            # Navigate to company directory
            os.chdir(self.company_dir)
    
            # Create the project directory
            os.makedirs(self.project_name, exist_ok=True)
    
            # Change to the project directory
            os.chdir(self.project_name)

            # Notifying user about project creation in progress
            print(f"\nStarting project creation for project name '{self.project_name}' and python version {self.python_version}\n")
            
            self.log(f"Directories for project '{self.project_name}' under company '{self.company_name}' created successfully.")
        
        except Exception as e:
            self.log(f"Error while creating directories for project '{self.project_name}' under company '{self.company_name}': {str(e)}", level="error")
            print("An error occurred while creating the directories. Check the log file for details.")

    def create_conda_env(self):
        try:
            # Check if environment already exists
            if check_existing_env(self.project_name):
                choice = input(f"Conda environment {self.project_name} already exists. Overwrite? (y/n): ")
                if choice.lower() != 'y':
                    print("Exiting.")
                    return

            # Create the Conda environment
            result = subprocess.run(["conda", "create", "--name", self.project_name, f"python={self.python_version}", "-y"],
                                    capture_output=True, text=True)
            
            self.log(result.stdout)
            
            if result.stderr:
                self.log(result.stderr, level="error")
            
            print(f"\nConda environment '{self.project_name}' created successfully.")
            print(f"\nActivate environment by using command:\n\nconda activate {self.project_name}\n\n")
        
        except Exception as e:
            self.log(str(e), level="error")
            print("An error occurred while creating the Conda environment. Check the log file for details.")

    def create_files(self):
        try:
            # List of standard filenames
            filenames = ["README.md", ".gitignore", "requirements.txt", ".env"]
            
            for filename in filenames:
                # Check if the file already exists
                if os.path.exists(filename):
                    choice = input(f"File {filename} already exists. Overwrite? (y/n): ")
                    if choice.lower() != 'y':
                        continue
                
                # Create and write initial content to the file
                with open(filename, "w") as f:
                    if filename == "README.md":
                        f.write(f"# {self.project_name}\n")
                    elif filename == ".gitignore":
                        f.write("env/\n__pycache__/\n")
                    elif filename == "requirements.txt":
                        f.write("# Add your project dependencies here\n")
                    elif filename == ".env":
                        f.write("# Add your environment variables here\n")
            
            self.log(f"Standard files for project '{self.project_name}' created successfully.")
            print("\nStandard files created successfully.")
        
        except Exception as e:
            self.log(str(e), level="error")
            print("An error occurred while creating the standard files. Check the log file for details.")

    def git_init(self):
        try:
            # Initialize Git repository
            subprocess.run(["git", "init"], capture_output=True, text=True)
            
            # Stage all files
            subprocess.run(["git", "add", "."], capture_output=True, text=True)
            
            # Make an initial commit
            subprocess.run(["git", "commit", "-m", "Initial commit"], capture_output=True, text=True)
            
            self.log(f"Git repository for project '{self.project_name}' initialized and initial commit made.")
            print("\nLocal Git repository initialized and initial commit made.")
        
        except Exception as e:
            self.log(str(e), level="error")
            print("An error occurred while initializing the Git repository. Check the log file for details.")

    def install_required_packages(self):
        try:
            # Install PyGithub
            subprocess.run(["pip", "install", "PyGithub"], capture_output=True, text=True)
            self.log(f"Required package PyGithub installed successfully.")
            print("\nRequired package PyGithub installed.")
        
        except Exception as e:
            self.log(str(e), level="error")
            print("An error occurred while installing the required packages. Check the log file for details.")

    def create_github_repo(self):
        choice = input("Would you like to create a new GitHub repository for this project? (y/n): ")
        if choice.lower() != 'y':
            self.log("User opted not to create a GitHub repository.", level="info")
            print("Skipping GitHub repository creation.")
            return None

        try:
            # Attempt to import Github class
            try:
                from github import Github
            except ImportError:
                self.install_required_packages()
                from github import Github
            
            # Ask user if they want to create a new GitHub repository
            choice = input("\nConfirm you would like to create a new GitHub repository. (y/n): ")
            if choice.lower() != 'y':
                return

            # Authenticate with GitHub
            token = self.github_token
            if not token:
                token = input("\nEnter your GitHub Personal Access Token: ").strip()
            
            try:
                g = Github(token)

                # Create new GitHub repository
                user = g.get_user()
                repo = user.create_repo(self.project_name)
            except Exception as e:
                print(f"Invalid GitHub token. Please check your token and try again. Error message: {e}")
                self.log("Invalid GitHub token provided.", level="error")
                return
                 
            self.log(f"GitHub repository for project '{self.project_name}' created successfully.")
            print(f"\nGitHub repository created: {repo.clone_url}")
            return repo.clone_url
        
        except Exception as e:
            self.log(str(e), level="error")
            print("An error occurred while creating the GitHub repository. Check the log file for details.")


    def link_github_repo(self, clone_url):
        try:
            # Link local repository to GitHub repository
            subprocess.run(["git", "remote", "add", "origin", clone_url], capture_output=True, text=True)
            
            # Push initial commit to remote repository
            subprocess.run(["git", "push", "-u", "origin", "master"], capture_output=True, text=True)
            
            self.log(f"Local repository for project '{self.project_name}' linked to GitHub repository.")
            print("\nLocal repository linked to GitHub and initial commit pushed.")
        
        except Exception as e:
            self.log(str(e), level="error")
            print("An error occurred while linking the local and GitHub repositories. Check the log file for details.")

    def push_github_repo(self):
        try:
            # Push changes to the GitHub repository
            subprocess.run(["git", "push"], capture_output=True, text=True)
            
            self.log(f"Changes for project '{self.project_name}' pushed to GitHub repository.")
            print("\nChanges pushed to GitHub repository.")
            
        except Exception as e:
            self.log(str(e), level="error")
            print("An error occurred while pushing changes to the GitHub repository. Check the log file for details.")


    def log(self, message, level="info"):
        if level == "info":
            logging.info(message)
        elif level == "error":
            logging.error(message)
        elif level == "warning":
            logging.warning(message)
        elif level == "debug":
            logging.debug(message)

    def check_token_expiration(self):
        try:
            expiration_date_str = "2023-12-25"
            expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d")
            
            # Check if the current date is greater than or equal to the expiration date
            if datetime.now() >= expiration_date:
                print("WARNING: Your GitHub token has expired. Please renew it.")
            else:
                remaining_days = (expiration_date - datetime.now()).days
                if remaining_days <= 30:  # Notify if the expiration date is within 30 days
                    print(f"NOTE: Your GitHub token will expire in {remaining_days} days.")
            
        except Exception as e:
            self.log(str(e), level="error")
            print("An error occurred while checking the GitHub token expiration. Check the log file for details.")

    def run(self):
        self.check_token_expiration()
        self.create_directories()
        self.create_conda_env()
        self.create_files()
        self.git_init()
        clone_url = self.create_github_repo()  # Store the clone URL
        if clone_url:  # Only proceed if clone_url is not None
            self.link_github_repo(clone_url)
            self.push_github_repo()
