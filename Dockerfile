FROM python:3.8.2-slim-buster

LABEL maintainer="Ronil Patel <ronil.patel@gmail.com>"

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD . /code/

RUN pip install -r requirements.txt

