import os

from .base import BASE_DIR

SECRET_KEY = '^#(3kwnb&g-3jp)u*4o_l5&*+v-fe(mahu&wgdjbu%8c*70qj#'

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
    }
}
