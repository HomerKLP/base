DJANGO_APPS = (
    'django.contrib.admin', 'django.contrib.staticfiles',
    'django.contrib.contenttypes', 'django.contrib.auth',
    'django.contrib.messages', 'django.contrib.sessions',
)

SIDE_APPS = (
    'corsheaders', 'rest_framework', 'django_extensions',
    'django_filters', 'django_fsm', 'silk', 'drf_yasg',
)

PROJECT_APPS = ('common',)

DEFAULT_APPS = DJANGO_APPS + SIDE_APPS + PROJECT_APPS
