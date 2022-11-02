# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster AS stage1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM stage1 AS stage2
RUN pip install numpy

FROM stage2 AS stage3
RUN pip install -U pytest coverage
COPY . .

# comment to make build-docker-image workflow run