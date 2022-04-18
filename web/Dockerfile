FROM ubuntu:20.04

RUN mkdir /codes/
WORKDIR codes

COPY mysite mysite
COPY sms sms
COPY Dockerfile Dockerfile
COPY manage.py manage.py
COPY requirements.txt requirements.txt
COPY mysite.uwsgi.ini mysite.uwsgi.ini
COPY db.sqlite3 db.sqlite3

RUN apt-get update && \
apt-get install -y python3.8 python3.8-dev python3.8-distutils python3.8-venv python3-pip

RUN pip install uwsgi daphne
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic

EXPOSE 8000
