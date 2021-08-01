cd toch
py -m venv toch-env
toch-env/Scripts/activate & pip install -r requirements.txt
cd toch
toch-env/Scripts/activate & main.py
