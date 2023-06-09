FROM python:3.8-slim-buster
ENV PYTHONBUFFERED=1
WORKDIR /dj-app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

