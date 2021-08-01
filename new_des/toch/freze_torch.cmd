rem @echo off
rem cd toch
rem venv-run main.py
rem pause
rem cmd /k "cd /d C:\Users\Admin\Desktop\venv\Scripts & activate & cd /d    C:\Users\Admin\Desktop\helloworld & python manage.py runserver"
rem pause
rem cmd /k "toch-env\Scripts\activate & main.py"
cmd /k "toch-env\Scripts\activate & pip freeze > requirements.txt"
rem python main.py
pause
