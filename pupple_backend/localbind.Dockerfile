FROM python:3.10.0


RUN apt-get update

Run pip install psycopg2
Run pip install psycopg2-binary
RUN pip freeze > requirements.txt
RUN pip install -r "requirements.txt"
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py runserver 0.0.0.0:8000
EXPOSE 8000

