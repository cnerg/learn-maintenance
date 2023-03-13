ARG PY_VERSION=3.8
ARG MESSAGE="default messsage"
# syntax=docker/dockerfile:1

FROM python:$PY_VERSION AS stage1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN echo stage1 MESSAGE = ${MESSAGE}

FROM stage1 AS stage2A
RUN echo stage2A MESSAGE = ${MESSAGE}

FROM stage2A AS stage2B
RUN echo stage2B MESSAGE = ${MESSAGE}

FROM stage1 AS stage3A
RUN pip install numpy
RUN echo stage3A MESSAGE = ${MESSAGE}

FROM stage3A AS stage3B
RUN pip install -U pytest coverage
COPY . .
RUN echo stage3B MESSAGE = ${MESSAGE}
