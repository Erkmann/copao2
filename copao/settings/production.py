import os

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = [
    'copao.fabricadesoftware.ifc.edu.br'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'copao',
        'USER': 'copao',
    }
}
