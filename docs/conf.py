# -*- coding: utf-8 -*-
#
# Flask-Pure documentation build configuration file
import os
import sys

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.insert(0, PROJECT_DIR)
import flask_pure  # noqa

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

source_suffix = '.rst'

master_doc = 'index'

project = u'Flask-Pure'
copyright = u'2016, Philip Xu and contributors'
author = u'Philip Xu and contributors'

release = flask_pure.__version__
version = release.rsplit('.', 1)[0]

language = None

exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = 'alabaster'
html_theme_options = {
    'github_banner': True,
    'github_repo': 'flask-pure',
    'github_user': 'pyx',
}

htmlhelp_basename = 'Flask-Puredoc'

latex_documents = [
    (master_doc, 'Flask-Pure.tex', u'Flask-Pure Documentation',
     u'Philip Xu', 'manual'),
]

man_pages = [
    (master_doc, 'flask-pure', u'Flask-Pure Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'Flask-Pure', u'Flask-Pure Documentation',
     author, 'Flask-Pure', 'One line description of project.',
     'Miscellaneous'),
]
