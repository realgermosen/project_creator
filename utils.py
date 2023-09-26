import subprocess

def check_existing_env(env_name):
    result = subprocess.run(["conda", "env", "list"], capture_output=True, text=True)
    envs = result.stdout.splitlines()
    for env in envs:
        if env_name in env:
            return True
    return False
