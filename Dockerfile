# syntax=docker/dockerfile:1

FROM python:3.11.0rc1-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install numpy
RUN pip install -U pytest coverage coveralls PyYAML
COPY . .