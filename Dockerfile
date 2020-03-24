FROM python:3.7-alpine
MAINTAINER Omer Mert Eksioglu

ENV PYTHONUNBUFFERED 1

COPY ./requerments.txt /requerments.txt
RUN pip install -r /requerments.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
