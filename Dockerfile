ARG PY_VERSION=3.8
ARG MESSAGE="default messsage"
# syntax=docker/dockerfile:1

FROM python:$PY_VERSION AS stage1
ARG MESSAGE
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN echo stage1 MESSAGE = ${MESSAGE}

FROM stage1 AS stage2a
RUN echo stage2a MESSAGE = ${MESSAGE}

FROM stage2a AS stage2b
RUN echo stage2b MESSAGE = ${MESSAGE}

FROM stage1 AS stage3a
RUN pip install numpy
RUN echo stage3a MESSAGE = ${MESSAGE}

FROM stage3a AS stage3b
RUN pip install -U pytest coverage
COPY . .
RUN echo stage3b MESSAGE = ${MESSAGE}
RUN echo something
