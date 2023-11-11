import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)
project_name="MLPROJECT"
list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingetion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_traning.py",
    f"src/{project_name}/components/data_monitoring.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exceptions.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "Dockerfile","app.py"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Create directory:{filedir} for the file {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")



