FROM python:3.8-alpine

ARG BASE_PATH

WORKDIR /python
COPY ./$BASE_PATH/requirements/base.txt /python/base.txt
COPY app.py   ./

RUN pip install -r base.txt -t .
RUN rm -f base.txt