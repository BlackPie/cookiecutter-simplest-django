import os


PROJECT_PATH = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# AUTH_USER_MODEL = 'users.User'

SECRET_KEY = 'v2z7rw)bh96f!&t*p9^ud4ee@f_v9yerde=89%_ys5qot5pls6'

DEBUG = True

ALLOWED_HOSTS = []

ALLOW_EMAIL_SENDING = True
