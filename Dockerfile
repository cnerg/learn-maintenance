# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install numpy
RUN pip install -U pytest coverage
COPY . .

# comment to make build-docker-image workflow run