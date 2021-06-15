# syntax=docker/dockerfile:1


FROM python:3.8

WORKDIR /app

ENV PYTHONBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

# RUN apt-get update && apt-get install gcc python3-dev musl-dev

RUN pip3 install --upgrade pip

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt    

COPY . . 



# previous configs
# FROM python:3.8

# ENV PYTHONBUFFERED 1

# WORKDIR /usr/src/crm_makers

# COPY ./requirements.txt /usr/src/requirements.txt

# RUN pip3 install -r /usr/src/requirements.txt 

# COPY . /usr/src/crm_makers

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
