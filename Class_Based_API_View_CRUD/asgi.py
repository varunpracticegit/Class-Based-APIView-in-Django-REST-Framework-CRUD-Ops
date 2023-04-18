"""
ASGI config for Class_Based_API_View_CRUD project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Class_Based_API_View_CRUD.settings')

application = get_asgi_application()
