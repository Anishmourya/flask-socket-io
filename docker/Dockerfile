FROM python:3.7.6-alpine3.10
MAINTAINER Anish Dhanka <anish.mourya5@gmail.com>

RUN pip install --upgrade pip

# add gcc for gevent
RUN apk add --no-cache gcc musl-dev

RUN apk add py-gunicorn

# pip cache for docker build
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app
COPY . /app/
ENV PYTHONPATH=/app
ENV GUNICORN_WORKER=5

ENTRYPOINT ["/entrypoint.sh"]
