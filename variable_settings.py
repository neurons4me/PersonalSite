'''
Settings that should differ between dev and prod environments go here.
Be careful when deploying to prod. If master branch has the wrong set
uncommented it will crash. Again, remember when deploying.
'''

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Development Settings
#

# DEBUG = True
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Production Settings
# -Uncomment below and comment out above before pushing to prod

DEBUG = False
ALLOWED_HOSTS = ['adam-mcdaniel.com',
                 '134.209.56.22',
                 'localhost',
                 'www.adam-mcdaniel.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
