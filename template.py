import os
from pathlib import Path        #to handle mac (/) to windows (\) file paths
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",                       # .github will be use for CI/CD deployment/comitting from github to cloud
    f"src/{project_name}/__init__.py",                # __init__.py is the constructor
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",                                   # Docker file is used for deployment
    "requirements.txt",                             # requirements.txt is used for 
    "setup.py",                                     # setup.py is used for local package setup
    "research/trials.ipynb",                         # trials.ipynb is used for research trials
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)                       # to handle mac (/) to windows (\) file paths
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)         # to create the directory if it doesn't exist
        logging.info(f"Created directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:                  # to create the file if it doesn't exist
            pass                                        # empty file will be created
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")