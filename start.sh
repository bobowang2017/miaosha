#!/bin/bash
ps -aux | grep 8888 | awk '{print $2}' | xargs kill -9
gunicorn miaosha.wsgi:application -b 0.0.0.0:8888 -w 8 -t 300 --reload

# gunicorn miaosha.wsgi:application -b 0.0.0.0:8888 -w 8 -k gthread --threads 40 --max-requests 4096 --max-requests-jitter 512