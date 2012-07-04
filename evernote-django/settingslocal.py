DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'evervim',
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'fire',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

EVERNOTE_HOST = "sandbox.evernote.com"
EVERNOTE_KEY = "akhaku"
EVERNOTE_SECRET = "45bcf3438ac20698"
EVERNOTE_OAUTH_COMPLETE_URL = "/"
EVERNOTE_OAUTH_TOKEN_VALIDITY = 1 
