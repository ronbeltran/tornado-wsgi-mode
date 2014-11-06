#!/bin/bash
gunicorn -w 4 wsgi:application
