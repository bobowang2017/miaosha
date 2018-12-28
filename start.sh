#!/bin/bash
ps -aux | grep 8888 | awk '{print $2}' | xargs kill -9
gunicorn miaosha.wsgi:application -b 0.0.0.0:8888 -w 4 -t 300 --reload