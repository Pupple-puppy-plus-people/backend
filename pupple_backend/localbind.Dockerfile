FROM python:3.10.0


RUN apt-get update

Run pip install psycopg2
Run pip install psycopg2-binary
RUN pip install -r requirements.txt

EXPOSE 8000

