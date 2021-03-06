"""
Django settings for steepshot_io project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('DJANGO_DEBUG'):
    DEBUG = os.getenv('DJANGO_DEBUG') == 'True'
else:
    DEBUG = False

if os.getenv('DJANGO_LOCAL'):
    LOCAL = os.getenv('DJANGO_LOCAL') == 'True'
else:
    LOCAL = False

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [
        'www.steepshot.io', 'steepshot.io', '159.203.87.66']

PROJECT_NAME = 'steepshot_io'

STEEM_NODE = 'wss://steemd.steemit.com'
GOLOS_NODE = 'wss://ws.golos.io'

IS_STEEM_CHAIN = True
IS_GOLOS_CHAIN = not IS_STEEM_CHAIN

if IS_STEEM_CHAIN:
    CURRENT_NODE = STEEM_NODE
elif IS_GOLOS_CHAIN:
    CURRENT_NODE = GOLOS_NODE
else:
    CURRENT_NODE = u''


STEEM_V1 = 'https://steepshot.org/api/v1'
STEEM_V1_1 = 'https://steepshot.org/api/v1_1'
STEEM_QA_V1 = 'https://qa.steepshot.org/api/v1'
GOLOS_V1 = 'https://golos.steepshot.org/api/v1'
GOLOS_QA_V1 = 'https://qa.golos.steepshot.org/api/v1'


REQUESTS_URL = {
    'active_users_monthly': '{url}/user/active/monthly',
    'user_sessions_daily': '{url}/user/count/sessions',
    'new_users_daily': '{url}/user/count/daily',
    'new_users_monthly': '{url}/user/count/unique',
    'new_users_percent_daily': '{url}/user/percent/unique',
    'DAU': '{url}/user/active/daily',
    'DAU_new_users': '{url}/user/active/new',

    'posts_average_per_author': '{url}/posts/average/author',
    'posts_payout_users': '{url}/posts/user-payout/daily',
    'posts_count_daily': '{url}/posts/count/daily',
    'posts_count_new_users': '{url}/posts/count/new/users',
    'posts_count_monthly': '{url}/posts/count/monthly',
    'posts_fee_daily': '{url}/posts/benefeciary-payout/daily',
    'posts_fee_weekly': '{url}/posts/fee/weekly',
    'posts_fee_author': '{url}/posts/fee/author',
    'posts_fee_users': '{url}/posts/fee/users',
    'posts_ratio_daily': '{url}/posts/ratio/daily',
    'posts_ratio_monthly': '{url}/posts/ratio/monthly',
    'posts_new': '{url}/posts/new',
    'posts_sharing': '{url}/stats/posts/sharing',

    'timeouts_daily': '{url}/stats/timeouts/daily',
    'ltv_daily': '{url}/stats/ltv',

    'count_top': '{url}/request/count/top',
    'count_hot': '{url}/request/count/hot',
    'count_new': '{url}/request/count/new',

    'browse_users_count_new': '{url}/browse/users/count/new',
    'browse_users_count_top': '{url}/browse/users/count/top',
    'browse_users_count_hot': '{url}/browse/users/count/hot',

    'count_comments_weekly': '{url}/posts/count/comments',
    'comments_percentage': '{url}/stats/comments/percentage',

    'count_votes_weekly': '{url}/posts/count/votes',
    'votes_average_weekly': '{url}/posts/average/votes',

    'delegators_steepshot': '{url}/stats/delegators/full'
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'googlecharts',
    'widget_tweaks',

    'steepshot_io.core',
    'steepshot_io.graph',
    'steepshot_io.table_stats',
    'steepshot_io.dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'steepshot_io.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_PATH, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'steepshot_io.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

USE_REDIS = True
if USE_REDIS:
    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
else:
    BROKER_URL = 'django://'
# Safe serializer settings
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/uploads/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

ADMIN_URL = r'^djadmin/'


DEFAULT_DATE_FORMAT = "%Y-%m-%d"
