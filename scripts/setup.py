# scripts/setup.py
import os
import subprocess

def setup_environment():
    """Create necessary directories and environment"""
    # Create directories
    directories = [
        'data/raw',
        'data/processed',
        'src/data',
        'src/models',
        'src/api',
        'tests',
        'notebooks'
    ]
    
    for dir in directories:
        os.makedirs(dir, exist_ok=True)
        
    # Create __init__.py files
    for dir in ['src/data', 'src/models', 'src/api']:
        with open(f'{dir}/__init__.py', 'w') as f:
            pass

    # Install requirements
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

if __name__ == "__main__":
    setup_environment()