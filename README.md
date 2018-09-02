# AbbidynThrowaway
A throwaway prototype

Completed User registration module fully

To use:

$ git clone https://github.com/vasanthn7/AbbidynThrowaway.git

$ cd AbbidynThrowaway/

$ virtualenv -p python3 env

$ source env/bin/activate

$ pip install -r requirements.txt

$ cd abbidyn/

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver

open http://127.0.0.1:8000/

PS: also install mysqld and mysql-dev
  : Create a database called Abbidyn in mysql before running the other commands
