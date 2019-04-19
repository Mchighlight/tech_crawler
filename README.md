# Web crawler
create a website aggregate 10 AI-related news each from Bloomberg technology and TNW, using python.
# About
create a website aggregate 10 AI-related news each from Bloomberg technology and TNW, using python.
trello: https://trello.com/b/mSgLmYGB/deveploment-process
![alt text](https://i.imgur.com/VA2j4Rm.jpg)
### Domain
http://henryhuang.pro/
# Develop Environment
Windows 10 Home
# Usage
Django
Django Rest framework
some bootrap4 and javascript
Python 
Celery
Rabbitmq
Postgresql
google cloud platform
## Local
複製專案
```
git clone XXX
```
建立virtual environment
```
py -m virtualenv venv
```
啟動virtual environment
```
.\venv\Scripts\activate
```
安裝packages
```
pip install -r requirements.txt
```
Migrations
```
python manage.py makemigrations && python manage.py migrate
```
Create superuser
```
python manage.py createsuperuser
```
collect static file
```
python manage.py collectstatic
```
local起server
```
python manage.py runserver 8000
```
The server will then be available at http://127.0.0.1:8000
## Docker
未實作
