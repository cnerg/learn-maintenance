ARG PY_VERSION=3.8
# syntax=docker/dockerfile:1

FROM python:$PY_VERSION AS stage1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN echo stage1

FROM stage1 AS stage2
RUN pip install numpy
RUN echo stage2

FROM stage2 AS stage3
RUN pip install -U pytest coverage
COPY . .
