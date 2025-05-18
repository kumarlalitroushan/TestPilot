import os
import django
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dashboard')))

def pytest_configure():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testpilot.settings")
    django.setup()