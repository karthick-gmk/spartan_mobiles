from myapp.wsgi import application
import os
import django
from django.core.management import execute_from_command_line

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

# Run migrations and create sample data
try:
    execute_from_command_line(['manage.py', 'migrate', '--noinput'])
    execute_from_command_line(['manage.py', 'create_sample_data'])
except Exception as e:
    print(f"Migration error: {e}")

app = application