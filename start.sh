#!/usr/bin/env bash
gunicorn blog_project.wsgi:application --preload --log-file -