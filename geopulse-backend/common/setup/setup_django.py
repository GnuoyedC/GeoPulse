import os
import sys
from django.conf import settings
from pathlib import Path

def config_exists():
    from django.conf import settings
    return settings.configured

def setup_django():
    if config_exists():
        from setup_warnings.setup_warnings import (ShowWarning)
        ShowWarning('SETUP_EXISTS')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.common')
        import django
        django.setup()
        
        return settings
def setup():
    if 'DJANGO_SETTINGS_MODULE' not in os.environ:
        # Running outside of Django
        sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
        setup_django()

if __name__ == '__main__':
    # Check if the script is run directly or imported
    setup()
