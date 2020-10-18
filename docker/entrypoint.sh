#!/bin/sh

exec gunicorn  run:app -b 0.0.0.0:5000  -w 5 -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker --worker-connections 1000