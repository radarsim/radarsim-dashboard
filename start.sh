#!/bin/sh

gunicorn --timeout=600 --workers=5 --threads=2 -b 0.0.0.0:9000 app:server
