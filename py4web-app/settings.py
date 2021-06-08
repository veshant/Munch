"""
This is an optional file that defined app level settings such as:
- database settings
- session settings
- i18n settings
This file is provided as an example:
"""
import os
from py4web.core import required_folder
from .private.secret_settings import *

# db settings
APP_FOLDER = os.path.dirname(__file__)
APP_NAME = os.path.split(APP_FOLDER)[-1]
# DB_FOLDER:    Sets the place where migration files will be created
#               and is the store location for SQLite databases
DB_FOLDER = required_folder(APP_FOLDER, "databases")
DB_URI = "sqlite://storage.db"
DB_POOL_SIZE = 1
DB_MIGRATE = True
DB_FAKE_MIGRATE = False  # maybe?

# Google Cloud Database
CLOUD_DB_URI = "google:MySQLdb://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?unix_socket=/cloudsql/{DB_CONNECTION}".format(
    DB_USER=DB_USER,
    DB_NAME=DB_NAME,
    DB_PASSWORD=DB_PASSWORD,
    DB_CONNECTION=DB_CONNECTION
)
CLOUD_DB_POOL_SIZE = 1
CLOUD_DB_MIGRATE = False # IMPORTANT!
CLOUD_DB_FAKE_MIGRATE = False

# location where static files are stored:
#STATIC_FOLDER = required_folder(APP_FOLDER, "static")

# location where to store uploaded files:
#UPLOAD_FOLDER = required_folder(APP_FOLDER, "uploads")

# send email on regstration
VERIFY_EMAIL = False

# account requires to be approved ?
REQUIRES_APPROVAL = False

# ALLOWED_ACTIONS:
# ["all"]
# ["login", "logout", "request_reset_password", "reset_password", "change_password", "change_email", "update_profile"]
# if you add "login", add also "logout"
ALLOWED_ACTIONS = ["all"]


# email settings
SMTP_SSL = True
SMTP_SERVER = "smtp.sendgrid.net"
SMTP_SENDER = "app@letsmunch.app"
# SENDGRID API KEY: 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
SMTP_LOGIN = "YXBpa2V5:U0cuZmw3MlBqVXRRZ0dzcFRyR3oxRWRIUS5WOThraFRkTk9rZXFDaDBLaS1aRDFuRHBJU0lmT2V2SlJWcjBMbWNfcXBv"
SMTP_TLS = False

# session settings
SESSION_TYPE = "database"
SESSION_SECRET_KEY = "6aea6573-7b40-441d-8170-2984874719c6" # replace this with a uuid
MEMCACHE_CLIENTS = ["127.0.0.1:11211"]
REDIS_SERVER = "localhost:6379"

# logger settings
LOGGERS = [
    "warning:stdout"
]  # syntax "severity:filename" filename can be stderr or stdout

# single sign on Google (will be used if provided)
OAUTH2GOOGLE_CLIENT_ID = None
OAUTH2GOOGLE_CLIENT_SECRET = None

# single sign on Okta (will be used if provided. Please also add your tenant
# name to py4web/utils/auth_plugins/oauth2okta.py. You can replace the XXX
# instances with your tenant name.)
OAUTH2OKTA_CLIENT_ID = None
OAUTH2OKTA_CLIENT_SECRET = None

# single sign on Google (will be used if provided)
OAUTH2FACEBOOK_CLIENT_ID = None
OAUTH2FACEBOOK_CLIENT_SECRET = None

# enable PAM
USE_PAM = False

# enable LDAP
USE_LDAP = False
LDAP_SETTINGS = {
    "mode": "ad",
    "server": "my.domain.controller",
    "base_dn": "ou=Users,dc=domain,dc=com",
}

# i18n settings
T_FOLDER = required_folder(APP_FOLDER, "translations")

# Celery settings
USE_CELERY = False
CELERY_BROKER = "redis://localhost:6379/0"

# try import private settings
try:
    from .settings_private import *
except (ImportError, ModuleNotFoundError):
    pass