# import os
# import sys
# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration
# from take5_api.settings import base
# from take5_api.settings.base import *  # noqa: F401, F403
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from pathlib import Path
from discere_linguis_api.settings.base import *  # noqa: F401, F403

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
ROOT_URLCONF = 'discere_linguis_api.urls'
# TEMPLATE_DEBUG = DEBUG
# APPLICATION_URL = 'https://dev.academiaalba.com/'
# CLOUDFRONT_URL = 'https://devapi.academiaalba.com/'
# SYSTEM_NAME = 'DEV - Academia Alba'
# SYSTEM_EMAIL_NAME = SYSTEM_NAME
# SYSTEM_EMAIL = 'suporte@take5.com.br'
# PRIMARY_COLOR = '#002A68'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '10.0.2.2']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'discere_linguis_dev',
    }
}
# # Amazon AWS
# AWS_ACCESS_KEY_ID = os.environ.get('OLD_DEV_AWS_ACCESS_KEY_ID', None)
# AWS_SECRET_ACCESS_KEY = os.environ.get('OLD_DEV_AWS_ACCESS_KEY_SECRET', None)
# AWS_STORAGE_BUCKET_NAME = 'django-academiaalba-dev'
# BUCKET_NAME = AWS_STORAGE_BUCKET_NAME
# AWS_STORAGE_REGION = 'sa-east-1'
# AWS_S3_CUSTOM_DOMAIN = '{0}.s3-{1}.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME, AWS_STORAGE_REGION)
# AWS_S3_URL = "https://%s/" % (AWS_S3_CUSTOM_DOMAIN)
# STATIC_URL = APPLICATION_URL + base.AWS_LOCATION
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, 'media')
# BUCKET_URL = AWS_S3_URL
# # Google FCM
# FCM_DJANGO_SETTINGS = {
#     'FCM_SERVER_KEY': 'AAAAuws0vlo:APA91bETPdNURSWTsry-XhmnOK8sDgMzgQVJY0J3q92Tmt3-oO_oYw29L-imUfneS2eU_lEgD894dUvqHly_a8KTpXZTniOIu6zxDBByV4rvYCVW-INgWpmq2y0F0QqcwtGyaNgpOGYp',
#     'DELETE_INACTIVE_DEVICES': True,
# }
# # One Signal
# FCM_ONESIGNAL = {
#     'AUTH': 'OWNiMmI5YjAtYzFkNC00MmI0LTgyZGUtZjU5NzI0N2M3Zjk0',
#     'APP_ID': '053a73fb-5c1f-426b-a89f-d934f263421b'
# }

# # Google Cloud
# GOOGLE_APPLICATION_CREDENTIALS = 'take5_api/settings/dev/google_cloud/dev-academiaalba-google.json'
# GOOGLE_APPLICATION_ACTIVE = True
# GOOGLE_APPLICATION_RANKING = True
# GOOGLE_RECAPTCHA_KEY = None
# GOOGLE_RECAPTCHA_SECRET = None
# # Sentry
# this_system_url = CLOUDFRONT_URL
# if len(sys.argv) >= 2:
#     if sys.argv[1] == 'runserver':
#         this_system_url = 'http://localhost:8000'
# if 'localhost' not in this_system_url:
#     sentry_sdk.init(
#         dsn="https://86f1604c18124c6396928e19db96ddd1@o261530.ingest.sentry.io/5520345",
#         integrations=[DjangoIntegration()],
#         ignore_errors=sentry_ignore_errors,  # noqa: F405
#         release="academiaalba-dev@" + base.SENTRY_SYSTEM_VERSION
#     )

# URL_ETRAINING_GROUP_TRAINING_SCORM = CLOUDFRONT_URL
# # GOOGLE_BIGQUERY_BUCKET = 'CORAL'
# # AKNA - INTEGRAÇÃO SMS
# AKNA_SENDER = 'Academia Alba'
# USE_CLOUDFRONT_SIGNATURE = True
