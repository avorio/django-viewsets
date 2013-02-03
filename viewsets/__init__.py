# coding: utf-8

from __future__ import unicode_literals
try:
    from .base import ViewSet
    from .model import ModelViewSet
# Allows to see module metadata outside of a Django project
# (including setup.py).
except ImportError:
    pass
from .patterns import PK, SLUG


__author__ = 'Bertrand Bordage'
__credits__ = ('Bertrand Bordage',)
__license__ = 'BSD License'
__version__ = '0.1.4.post'
__maintainer__ = 'Bertrand Bordage'
__email__ = 'bordage.bertrand@gmail.com'
__status__ = '3 - Alpha'
