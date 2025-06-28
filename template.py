import os
import logging
from pathlib import Path

# This controls how the log messages are formatted when displayed.
# %(asctime)s: Inserts the current timestamp
# %(message)s: Inserts the log message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_title = "TextSummarizer"

#list of all files in the project directory
files=[
    ".github/workflows/gitkeep",
    f"source/{project_title}/__init__.py",
    f"source/{project_title}/components/__init__.py",
    f"source/{project_title}/utils/__init__.py",
    f"source/{project_title}/utils/common.py",
    f"source/{project_title}/logging/__init__.py",
    f"source/{project_title}/config/__init__.py",
    f"source/{project_title}/config/config.py",
    f"source/{project_title}/pipeline/__init__.py",
    f"source/{project_title}/entity/__init__.py",
    f"source/{project_title}/constants/__init__.py",
    "config/config.yaml",
    "parameters.yaml",
    "application.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "experiments/trials.ipynb",
]

for file_path in files:
    path=Path(file_path)  #gives path in required format
    file_dir,file_name=os.path.split(path)  #splitting path into directory and file name

    if(file_dir !=""):   #file dir is empty means no folder exists
        os.makedirs(file_dir, exist_ok=True)  #create the directory if not exists
        logging.info(f"Created directory: {file_dir} for the file {file_name}")

    if(not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):   #if file doesn't exist then create it   
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Created file: {file_path}")    

    else:
        logging.info(f"File {file_path} already exists")
        


