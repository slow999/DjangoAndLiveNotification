FROM python:3.8-alpine

RUN apk add python3-dev build-base linux-headers pcre-dev libffi-dev

RUN mkdir /codes/
WORKDIR codes

COPY mysite mysite
COPY sms sms
COPY Dockerfile Dockerfile
COPY manage.py manage.py
COPY requirements.txt requirements.txt
COPY mysite.uwsgi.ini mysite.uwsgi.ini
COPY db.sqlite3 db.sqlite3
COPY gunicorn.app.conf.py gunicorn.app.conf.py
COPY gunicorn.channel.conf.py gunicorn.channel.conf.py

RUN pip install gunicorn uvicorn[standard]
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic

EXPOSE 8000
