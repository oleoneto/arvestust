# coding: utf-8
"""
    arvestust is a django app with support for file management.
"""
from __future__ import unicode_literals
from .requires import REQUIRED_APPS

__version__ = "0.6.0"
__license__ = 'BSD 3-Clause'
__copyright__ = 'Copyright 2020 Lehvitus ÖU'

VERSION = __version__

default_app_config = 'arvestust.apps.ArvestustConfig'
