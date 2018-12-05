FROM python:3.7-alpine
LABEL version="1.0"
LABEL maintainer="joy.calcutta@gmail.com"

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# copy project
COPY . /usr/src/app/

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
# RUN pip install gunicorn
RUN pipenv install
