#!/bin/bash
echo \"Running migrations...\"\npython manage.py makemigrations --noinput\npython manage.py migrate --noinput\necho \"Migrations completed\"