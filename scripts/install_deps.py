import subprocess

def install_dependencies():
    """Install project dependencies"""
    packages = [
        'torch',
        'torchvision',
        'fastapi',
        'uvicorn',
        'numpy',
        'pandas',
        'python-dotenv',
        'scikit-learn',
        'matplotlib'
    ]
    
    for package in packages:
        subprocess.run(['pip', 'install', package])

if __name__ == "__main__":
    install_dependencies()