import os

def init_project():
    """Initialize project configuration"""
    # Create .env file
    env_content = """PYTHONPATH=${PWD}
DATA_DIR=data/
MODEL_DIR=models/
"""
    with open('.env', 'w') as f:
        f.write(env_content)

if __name__ == "__main__":
    init_project()