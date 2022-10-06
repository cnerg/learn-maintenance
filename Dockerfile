ARG PY_VERSION=3.8
# syntax=docker/dockerfile:1
FROM python:$PY_VERSION
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install numpy
RUN pip install -U pytest coverage
COPY . .
# comment to make buildImage.yml workflow run