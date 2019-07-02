# flake8: noqa: F401,F403

import os
import sys

from copao.settings.base import *

env = os.environ.get('DJANGO_ENV', 'development')

if env == 'development':
    print('WARNING: Running in development mode.', file=sys.stderr)
    from copao.settings.development import *
elif env == 'production':
    from copao.settings.production import *
else:
    print('Invalid DJANGO_ENV "{}"'.format(env), file=sys.stderr)
    sys.exit(1)
