import argparse
from project_creator import ProjectCreator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new Python project with a Conda environment.')
    parser.add_argument('project_name', type=str, help='The name of the project')
    parser.add_argument('python_version', type=str, help='The Python version for the Conda environment')
    args = parser.parse_args()
    
    github_token = "your_github_token_here" # Replace with your actual GitHub token
    project_creator = ProjectCreator(args.project_name, args.python_version, github_token)
    project_creator.run()
