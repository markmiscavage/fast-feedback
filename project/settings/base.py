import os.path

# Include apps on the path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

# People who get code error notifications when DEBUG=False
ADMINS = (('Sbk Feedback administrator', 'mark.miscavage@smarkets.com'),)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'dev.db'),
    }
}

# Never deploy a site into production with DEBUG turned on!
DEBUG = True

# Address to use for various automated correspondence from the site manager(s).
DEFAULT_FROM_EMAIL = 'mark.miscavage@smarkets.com'

# Set the subject prefix for email messages sent to admins and managers
EMAIL_SUBJECT_PREFIX = '[Sbk Feedback] '

#DEFAULT_FROM_EMAIL = ''
#EMAIL_HOST = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

# Maximum size (in bytes) before an upload gets streamed to the file system.
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880

# List of locations of the fixture data files, in search order
FIXTURE_DIRS = ()

# A tuple of strings designating all the enabled applications
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    # scarlet requirements
    'taggit',
    # scarlet
    'scarlet.cms',
    'scarlet.versioning',
    'scarlet.assets',
    'scarlet.cache',
    'scarlet.scheduling',
    'apps.ff0000',  # load django-admin commands, initial fixtures, ..
    'apps.feedback',
)

# A tuple of IP addresses that see debug comments, when DEBUG is True
INTERNAL_IPS = ('0.0.0.0', '127.0.0.1',)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_SSL_PROXY', 'true')

# Number of items to show in a RSS Feed
ITEMS_PER_FEED = 5

# The language code for this installation
LANGUAGE_CODE = 'en-us'

# If login is successful, the view redirects to the URL specified in next.
# If next isn't provided, it redirects to settings.LOGIN_REDIRECT_URL
# (which defaults to /accounts/profile/).
LOGIN_REDIRECT_URL = '/admin'

# Who should get broken-link notifications when SEND_BROKEN_LINK_EMAILS=True
MANAGERS = ADMINS

# Absolute path to the directory that holds stored files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# URL that handles the media served from MEDIA_ROOT (must end in a slash)
MEDIA_URL = '/uploads/'

# A tuple of middleware classes to use
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'apps.ff0000.middleware.XUACompatibleMiddleware'
)

# Number of digits grouped together on the integer part of a number
NUMBER_GROUPING = 3

# The full Python import path to the root URLconf
ROOT_URLCONF = 'urls'

# Seed for secret-key hashing algorithms
SECRET_KEY = '8M96yJMqqoKMk5DV0Isrmn5ExpTsKwoV4rUObkySsSuIJwcTrR'

# Whether files other than .html should be returned with the correct MIME type
SET_MIMETYPE = True

# The ID of the current site in the django_site database table
SITE_ID = 1

# Absolute path to the directory where collectstatic will collect static files
STATIC_ROOT = os.path.join(BASE_DIR, 'collected-static')

# URL to use when referring to static files located in STATIC_ROOT
STATIC_URL = '/static/'

# Additional locations the staticfiles app will traverse
DEV_STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
SOURCE_STATIC_ROOT = os.path.join(PROJECT_ROOT, 'source')
STATICFILES_DIRS = (SOURCE_STATIC_ROOT, DEV_STATIC_ROOT)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'apps.ff0000.context_processors.settings',
    'apps.ff0000.context_processors.base_template',
)

TEMPLATE_DIRS = [STATIC_ROOT, os.path.join(PROJECT_ROOT, 'templates'), STATIC_ROOT]

if DEBUG:
    TEMPLATE_DIRS = [DEV_STATIC_ROOT, os.path.join(PROJECT_ROOT, 'templates'), DEV_STATIC_ROOT]


TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': TEMPLATE_DIRS,
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
            'apps.ff0000.context_processors.settings',
            'apps.ff0000.context_processors.base_template',
        ],
        'debug': DEBUG,
    },
}, ]
# Display a detailed report for any TemplateSyntaxError.
TEMPLATE_DEBUG = DEBUG


# List of locations of the template source files, in search order
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# A tuple of template loader classes, specified as strings
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# The time zone for this installation
TIME_ZONE = 'America/Los_Angeles'

# Output the "Etag" header. This saves bandwidth but slows down performance
USE_ETAGS = False

# Enable Django's internationalization system
USE_I18N = False

# Display numbers and dates using the format of the current locale
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Testing
TEST_RUNNER = 'testing.TestRunner'

# Which settings are passed by RequestContext to the templates
# Keep this list small, as it is passed to each request.
# Uncomment more settings as needed
VIEW_SETTINGS = (
    'LANGUAGE_CODE',
    'TEMPLATE_DEBUG',
    'PERM_STATIC_URL'
)

LOG_FILENAME = None
