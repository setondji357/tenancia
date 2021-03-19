"""
Django settings for meslimmo project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os
import datetime


AUTH_USER_MODEL = 'customuser.User'

SITE_ID = 1

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sz)!59k=#curo2j+bjlpzkx)pg3!mv7_hky!*z(h+n0iujt#fn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=0))

# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Application definition

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'corsheaders',
    'rest_framework',
    'social_django',
    'allauth',
    'allauth.account',
    'rest_framework_jwt',
    # 'rest_registration',
    'countries_plus'
)

LOCAL_APPS = (
    'customuser',
    'proprietaire',
    'banque',
    'contrat',
    'immeuble',
    # 'mauth',
    'appartement',
    # 'mcore',
    'quittance',
    'reglement',
    'societe',
    'tools',
    'client',
    'rest_graph_ql',
    # 'client' ,
    # 'rest_graph_ql',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS




MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'meslimmo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'meslimmo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE"),
        'NAME': os.environ.get("SQL_DATABASE"),
        'USER': os.environ.get("SQL_USER"),
        'PASSWORD': os.environ.get("SQL_PASSWORD"),
        'HOST': os.environ.get("SQL_HOST"),
        'PORT': os.environ.get("SQL_PORT"),
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tenancia_db',
        'USER': 'postgres',
        'PASSWORD': 'tenancia',
        'HOST': 'db',
        'PORT': '5433',
    }
}
"""
# Password validatirest_registeron
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = "/static/"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
if not os.path.join('LOGS'):
    os.mkdir('LOGS')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s '
                      '[%(name)s:%(lineno)s] {message}',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'verbose2': {
            'format': '[%(asctime)s] %(levelname)s'
                      ' [%(filename)s:%(lineno)s:%(funcName)s()] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'with_ip': {
            'format': '[%(asctime)s] [%(clientip)s] %(levelname)s %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'LOGS/debug.log',
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 5,
            'formatter': 'verbose'
        }, 'staff': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'LOGS/debug.log',
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 5,
            'formatter': 'with_ip'
        }, 'application': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'LOGS/NOTES.log',
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 5,
            'formatter': 'with_ip'
        }, 'ddyxdebug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'LOGS/debug.log',
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 5,
            'formatter': 'verbose2'
        }, 'other_sources': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'LOGS/OTHER_SOURCES.log',
            'maxBytes': 1024 * 1024 * 500,  # 100 MB
            'backupCount': 5,
            'formatter': 'verbose2'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'WARNING',
        },
        'staff': {
            'handlers': ['staff'],
            'level': 'INFO',
        },
        'application': {
            'handlers': ['application'],
            'level': 'INFO',
        },
        'other_sources': {
            'handlers': ['other_sources'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'asyncio': {
            'level': 'WARNING'
        }
    }
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'PASSWORD_RESET_SERIALIZER':
        'customuser.serializers.PasswordResetSerializer1',
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Remove username functionality. Email is identifier
# https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-user-models
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
REST_USE_JWT = True
OLD_PASSWORD_FIELD_ENABLED = True

# Email Settings
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SENDGRID_ECHO_TO_STDOUT = False
SENDGRID_API_KEY = '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'
DEFAULT_FROM_EMAIL = 'Tenancia'


# Load Social auth key in env
for key in ['GOOGLE_OAUTH2_KEY',
            'GOOGLE_OAUTH2_SECRET',
            'FACEBOOK_KEY',
            'FACEBOOK_SECRET']:
    exec("SOCIAL_AUTH_{key} = os.environ.get('{key}', '')".format(key=key))
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile']
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
# See here for more details:
# http://psa.matiasaguirre.net/docs/use_cases.html#associate-users-by-email
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # <- this line not included by default
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
REST_USE_JWT = True

# http://getblimp.github.io/django-rest-framework-jwt/
# JWT settings in setting.py file
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
        'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
        'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_payload_handler',
    # Specify a custom function to generate the token payload

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
        'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'customuser.views.jwt_response_payload_handler',
    # Responsible for controlling the response data returned after login or refresh.
    # Override to return a custom response such as including the serialized representation of the User
    # 'rest_framework_jwt.utils.jwt_response_payload_handler',

    # 'rest_framework_jwt.utils.jwt_response_payload_handler',
    # i have customize the response bkz i want user profile  and token as login

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    # You can turn off expiration time verification by setting
    # JWT_VERIFY_EXPIRATION to False. Without expiration verification,
    # JWTs will last forever meaning a leaked token could be used by an attacker indefinitely'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=12),
    #  This will be added to datetime.utcnow() to set the expiration time.
    # Default is datetime.timedelta(seconds=300)(5 minutes).
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    #  This is how much time after the original token that future tokens can be refreshed from.
    # Default is datetime.timedelta(days=7) (7 days).

    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': None,
}
BASE_API_URL = 'http://tenancia.com/api/v1/'
BASE_FRONT_URL = 'http://localhost:8080'
ALLOWED_HOSTS = ['http://localhost:8080', 'localhost']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    "http://tenancia.com",
    'http://localhost:8080',
    "http://127.0.0.1:8080"
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
APPEND_SLASH=False
RABBITMQ_HOST = 'localhost'
CELERY_BROKER_URL = 'amqp://' + RABBITMQ_HOST
TWILIO_ACCOUNT_SID = 'AC841b0c01be5608ad900f5fcd452a6172'
TWILIO_AUTH_TOKEN = 'e08b2c59fe5a6c4c674e2fdacefd3963'
# CELERY_BROKER_URL = 'amqp://rabbitmq'
# CELERY_BROKER_URL = 'amqp://guest@localhost'
# CELERY_BROKER_URL = "amqp://tenancia:tenancia@localhost:5672/"
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '515214403352-dd3itjg2aequg8387650rr1b8aefpovf.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'N8k7xSNPfjn4rJf5fvyVOAs7'


