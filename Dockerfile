FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . /code


COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
