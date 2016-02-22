# -*- coding: utf-8 -*-
# Copyright (c) 2016, Philip Xu <pyx@xrefactor.com>
# License: BSD New, see LICENSE for details.
"""Flask-Pure - a Flask extension for Pure.css"""

from flask import Blueprint, Markup, current_app, url_for

__version__ = '0.1'
__all__ = ['get_css_links', 'Pure']

CDN_PREFIX = 'http://yui.yahooapis.com/pure/0.6.0/'
LINK_TEMPLATE = '<link rel="stylesheet" href="%s">'


def get_css_links():
    """context processor to generate css link as ``purecss_stylesheets``"""
    if current_app.config['PURECSS_USE_MINIFIED']:
        pure_css = 'pure-min.css'
        grids_responsive = 'grids-responsive-min.css'
    else:
        pure_css = 'pure.css'
        grids_responsive = 'grids-responsive.css'

    if current_app.config['PURECSS_USE_CDN']:
        pure_css = CDN_PREFIX + pure_css
        grids_responsive = CDN_PREFIX + grids_responsive
    else:
        pure_css = url_for('pure.static', filename=pure_css)
        grids_responsive = url_for('pure.static', filename=grids_responsive)

    css = LINK_TEMPLATE % pure_css + '\n' + LINK_TEMPLATE % grids_responsive

    return {'purecss_stylesheets': Markup(css)}


class Pure(object):
    """Flask-Pure extension

    provides base template layout as :code:`pure/layout.html` and links to the
    Pure.css static assets.
    """
    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """create and register a blueprint with the Flask application.

        :param app:
            Flask application instance
        """
        app.config.setdefault('PURECSS_USE_CDN', True)
        app.config.setdefault('PURECSS_USE_MINIFIED', True)

        pure = Blueprint(
            'pure',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=app.static_url_path + '/pure/css')

        app.register_blueprint(pure)
        app.context_processor(get_css_links)

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions['pure'] = self
