#!/bin/bash
gunicorn -w 4 --access-logfile - wsgi:application
