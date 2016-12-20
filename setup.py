# -*- coding: utf-8 -*-
import re
from os import path
from setuptools import setup

ROOT_DIR = path.abspath(path.dirname(__file__))

DESCRIPTION = 'Flask-Pure - a Flask extension for Pure.css'
LONG_DESCRIPTION = open(path.join(ROOT_DIR, 'README.rst')).read()
VERSION = re.search(
    "__version__ = '([^']+)'",
    open(path.join(ROOT_DIR, 'flask_pure', '__init__.py')).read()
).group(1)


setup(
    name='Flask-Pure',
    version=VERSION,
    url='https://github.com/pyx/flask-pure/',
    license='BSD-New',
    author='Philip Xu and contributors',
    author_email='pyx@xrefactor.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=['flask_pure'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
    ],
    extras_require={
        'test': ['pytest>=2.8.2'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
