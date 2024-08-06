import os
from dotenv import load_dotenv

def load_environment_varibles():
    """
    Load the environment variables from main location
    """
    load_dotenv()

    env_vars = {
        "GROQ_API_KEY": os.getenv("GROQ_API_KEY")
    }

    return env_vars

def verify_environment_varibles(env_vars):
    """
    Checking - Loading variables
    """
    all_env_vars_set = True

    for key, value in env_vars.items():
        if not value:
            # print(f"{key} is not set!")
            all_env_vars_set = False

    return all_env_vars_set
