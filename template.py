import os
from pathlib import Path
import logging

project_name = 'cnnClassifier'

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for file in list_of_files:
    file = Path(file)
    filedir, filename = os.path.split(file)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory; {filedir} for the file: {filename}")

    if (not os.path.exists(file)):
        open(file, "a").close()
        logging.info(f"Created empty file: {file}")
    else:
        logging.info(f"{filename} is already exists")
