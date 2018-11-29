FROM python:3.7-alpine
LABEL version="1.0"
LABEL maintainer="joy.calcutta@gmail.com"

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install

# copy project
COPY . /usr/src/app/