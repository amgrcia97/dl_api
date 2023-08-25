from pathlib import Path
from discere_linguis_api.settings.base import *  # noqa: F401, F403

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False
ROOT_URLCONF = 'discere_linguis_api.urls'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '10.0.2.2']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'discerelinguis$prod',
        'USER': 'discerelinguis',
        'PASSWORD': '@OwP998M0*Z$',
        'HOST': 'discerelinguis.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
