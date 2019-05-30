#!/bin/bash
gunicorn $1 -c gunicorn/gunicorn.conf
