FROM public.ecr.aws/lambda/python:3.8

ARG BASE_PATH

WORKDIR /python
COPY ./$BASE_PATH/requirements/base.txt /python/base.txt
COPY .   ${LAMBDA_TASK_ROOT}

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r base.txt
RUN rm -f base.txt

CMD ["lambda_function.handler"]