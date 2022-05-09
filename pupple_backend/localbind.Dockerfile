FROM python:3.10.0


RUN apt-get update

RUN pip install psycopg2
RUN pip install psycopg2-binary
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

