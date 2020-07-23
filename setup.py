import os
import re
from setuptools import find_packages, setup


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('arvestust')

setup(
    version=version,
    name='django-arvestust',
    url='https://www.github.com/lehvitus/arvestust',
    author='Leo Neto',
    author_email='projects@lehvitus.com',
    description='A Django app for file management and record-keeping',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
)
