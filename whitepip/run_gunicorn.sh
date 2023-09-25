
source whitepip/venv/bin/activate

cd /django/whitepip

gunicorn your_project.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4
