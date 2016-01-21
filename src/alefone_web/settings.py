"""
Django settings for alefone_web project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#/home/santosh/code/alefone_web/src



#email related config
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'bsantoshraj@gmail.com'
EMAIL_HOST_PASSWORD = 'k1ngf1sh'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wuw--w$&_+mxadi(gn3)5-1dc9y^_2hxb3dx=6(4sntjosn3r9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/home/santosh/code/alefone_web/static/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.csrf',
                # 'allauth.account.context_processors.account',
               # 'allauth.socialaccount.context_processors.socialaccount',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend"
)




ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
#    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'profiles',
    'polls',
    'provider',
    'provider.oauth2',
    'tastypie',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
)

SITE_ID=1

CRISPY_TEMPLATE_PACK = 'bootstrap3'
#LOGIN_REDIRECT_URL = '/profile/'
#LOGIN_URL='/acounts/login/'
ACCOUNT_AUTHENTICATION_METHOD="username_email"
#ACCOUNT_USERNAME_REQUIRED=False
#ACCOUNT_EMAIL_REQUIRED=True
#ACCOUNT_USER_MODEL_USERNAME_FIELD=None
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
LOGIN_REDIRECT_URL='/'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_USER_DISPLAY = lambda user: user.get_short_name()
ACCOUNT_EMAIL_VERIFICATION = "optional"

#STRIPE INFO
#TEST KEYS
STRIPE_PUBLISHABLE_KEY  = 'pk_test_ewCzElJ9vuuc426wMqPUNMbn'
STRIPE_SECRET_KEY = 'sk_test_3iXHFWwjUtXOEICNCxf54bmy'


#LIVE KEYS
#STRIPE_PUBLISHABLE_KEY  = 'pk_live_qEq33XtDyB2AonDjzeokYNhi'
#STRIPE_SECRET_KEY = 'sk_live_Tvda7Kepq238nvTsyTpZvFnd'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'alefone_web.urls'

WSGI_APPLICATION = 'alefone_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
       #'/home/santosh/code/alefone_web/static/templates',
       os.path.join(os.path.dirname(BASE_DIR),"static","templates"),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#media is anything uploaded by user

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
#/home/santosh/code/alefone_web/static/media
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "root")
#STATIC_ROOT = '/home/santosh/code/alefone_web/static/root'
#/home/santosh/code/alefone_web/static/root
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static","static"),
)
#/home/santosh/code/alefone_web/static/static
