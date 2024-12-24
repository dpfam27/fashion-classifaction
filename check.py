import os
import pkg_resources
import importlib
import ast

def get_imports_from_file(file_path):
    """Extract imports from a Python file"""
    try:
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
            
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for name in node.names:
                    imports.add(name.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split('.')[0])
        return imports
    except:
        return set()

def scan_project_imports():
    """Scan all Python files in project for imports"""
    project_imports = set()
    
    # Walk through all Python files
    for root, dirs, files in os.walk('.'):
        if 'fashion-env' in root or '.git' in root:  # Skip env and git
            continue
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                project_imports.update(get_imports_from_file(file_path))
    
    return project_imports

def check_package_usage():
    # Get all installed packages
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    
    # Get actual imports used in project
    project_imports = scan_project_imports()
    
    results = []
    for package, version in installed_packages.items():
        if package in project_imports:
            results.append(f"{package} (v{version}): Used in project")
        else:
            try:
                importlib.import_module(package)
                results.append(f"{package} (v{version}): Installed but not directly used")
            except ImportError:
                results.append(f"{package} (v{version}): Not imported/May not be needed")
    
    return results

if __name__ == "__main__":
    print("Analyzing project dependencies...\n")
    for result in check_package_usage():
        print(result)