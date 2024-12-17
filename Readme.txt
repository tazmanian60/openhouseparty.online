run in command prompt before running app:
## (JK) SET FLASK_APP=C:\Repos\openhouseparty.online\flaskr.py
## (CM)
SET FLASK_APP=C:\Users\user\Documents\GitHub\openhouseparty.online\flaskr.py
C:\Users\user\AppData\Local\Programs\Python\Launcher\py.exe get-pip.py

then init the db:
flask initdb
## (JK) or flask init-db

then start server:
## (CM) flask run -h 127.0.0.1 -p 5000
python -m flask run

username for testing is:
admin
password for 'admin' user is:
testing

Test1234
Test1234
Test1234