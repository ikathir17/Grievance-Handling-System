"""
WSGI config for grievance_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.db import connection
from django.db.utils import OperationalError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grievance_system.settings')

# Create application first
application = get_wsgi_application()

# Add for Vercel
app = application

# Run migrations automatically in Vercel environment
if 'VERCEL' in os.environ:
    from django.core.management import call_command
    try:
        # Check if migrations need to be run
        call_command('migrate', '--noinput')
        print("Migrations completed successfully")
    except OperationalError as e:
        print(f"Migration error: {e}")
