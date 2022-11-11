ARG PY_VERSION=3.8
# syntax=docker/dockerfile:1

FROM python:$PY_VERSION AS stage1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM stage1 AS stage2
RUN pip install numpy

FROM stage2 AS stage3
RUN pip install -U pytest coverage
COPY . .
# make a change in stage3, see if all images are rebuilt
