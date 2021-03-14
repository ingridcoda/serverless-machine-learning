FROM public.ecr.aws/lambda/python:3.8

ARG BASE_PATH

WORKDIR /python
COPY ./$BASE_PATH/requirements/base.txt /python/base.txt
COPY lambda_function.py   ${LAMBDA_TASK_ROOT}

RUN pip install -r base.txt -t .
RUN rm -f base.txt

CMD ["lambda_function.handler"]