
import os, datetime, json, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import util
from django.core.exceptions import ImproperlyConfigured

SETTING_DIR = util.get_server_info_value("production")
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

MEDIA_ROOT = os.path.join(BASE_DIR, SETTING_DIR["MEDIA_ROOT"]) 
MEDIA_URL = SETTING_DIR["MEDIA_URL"]


#data 베이스 설정들 json파일로 옮김.
DATABASES = {
    'default': SETTING_DIR["DATABASES"]["default"]
}
SECRET_KEY = SETTING_DIR["SECRET_KEY"]

#jwt 관련 설정. - json으로 옮김
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': SETTING_DIR["JWT_AUTH"]["JWT_ALGORITHM"],
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': SETTING_DIR["JWT_AUTH"]["JWT_EXPIRATION_DELTA"],
    'JWT_REFRESH_EXPIRATION_DELTA': SETTING_DIR["JWT_AUTH"]["JWT_REFRESH_EXPIRATION_DELTA"],
}


#smtp 를 위한 설정들  host - port까지 json으로 옮김
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = SETTING_DIR["STMP_SETTING"]["EMAIL_HOST"]
EMAIL_HOST_USER = SETTING_DIR["STMP_SETTING"]["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = SETTING_DIR["STMP_SETTING"]["EMAIL_HOST_PASSWORD"]
EMAIL_PORT = SETTING_DIR["STMP_SETTING"]["EMAIL_PORT"]
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGIN_REDIRECT_URL = '/'

#restframework 와 jwt 설정
REST_FRAMEWORK = {
    #로그인 여부를 확인하는 클래스를 rest_framewor.permissons.IsAuthenticated 로 사용한다.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    #로그인과 관련된 클래스를 JSONWebTokenAuthentication 로 쓴다.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    SETTING_DIR["ALLOWED_HOSTS"]["1"],
    SETTING_DIR["ALLOWED_HOSTS"]["2"],
    SETTING_DIR["ALLOWED_HOSTS"]["3"],
    SETTING_DIR["ALLOWED_HOSTS"]["4"]
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 써드파티 앱
    'django_extensions',
    'imagekit',
    'rest_framework',
    
    'blog',
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

ROOT_URLCONF = 'config.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, SETTING_DIR["TEMPLATE_DIR"])

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'




# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = SETTING_DIR["STATIC_URL"]
STATIC_DIR = os.path.join(BASE_DIR, SETTING_DIR["STATIC_DIR"])
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(ROOT_DIR, SETTING_DIR["STATIC_ROOT"])
