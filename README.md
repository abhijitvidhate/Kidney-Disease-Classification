# Kidney-Disease-Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/abhijitvidhate/Assignment-1
```
### STEP 01 - Set up Python environment

Conda may not be available; the project works with a standard Python 3.8+ virtual environment. From the project root run:

```bash
python3 -m venv cnncls_env             
source cnncls_env/bin/activate          
pip install --upgrade pip setuptools wheel
```

### STEP 02 - Install dependencies

```bash
pip install -r requirements.txt
```

### STEP 03 - Run the application

Start MLflow tracking server (on port 5000):

```bash
mlflow ui --host 127.0.0.1 --port 5000
```

In another terminal, start the Flask web app (on port 8000):

```bash
python app.py
```

Open your browser at `http://127.0.0.1:8000` for the prediction UI and `http://127.0.0.1:5000` for MLflow.

Now,
```bash
open up you local host and port
```



## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### CMD

- mlflow ui

### DAGSHUB

[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/Kidney-Disease-Classification-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=entbappy \
MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/Kidney-Disease-Classification-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```


### DVC CMD

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)

