FROM python:3.10.0

COPY ./ /home/backend/pupple_backend

WORKDIR /home/backend/pupple_backend

RUN apt-get update

Run pip install psycopg2-binary
RUN pip install -r requirements.txt

EXPOSE 8000

