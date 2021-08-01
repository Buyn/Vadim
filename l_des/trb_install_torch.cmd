rem @echo off
cd toch
rem venv-run main.py
rem pause
rem cmd /k "cd /d C:\Users\Admin\Desktop\venv\Scripts & activate & cd /d    C:\Users\Admin\Desktop\helloworld & python manage.py runserver"
rem cmd /k "toch-env\Scripts\activate & main.py"
py -m venv toch-env
pause
cmd /k "toch-env\Scripts\activate & pip install -r requirements.txt"
pause
cd toch
cmd /k "toch-env\Scripts\activate & main.py"
rem pip freeze > requirements.txt
rem python main.py
pause
