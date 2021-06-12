# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ENV PYTHONBUFFERED 1

RUN mkdir -p ./app

WORKDIR /app

RUN apk add --update --no-cache postgresql-client jpeg-dev

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt 

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
