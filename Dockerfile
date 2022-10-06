# syntax=docker/dockerfile:1

FROM ubuntu:18.04
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install python-pip
RUN pip install -r requirements.txt
RUN pip install numpy
RUN pip install -U pytest coverage
COPY . .
