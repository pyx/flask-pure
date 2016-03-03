# -*- coding: utf-8 -*-
# Copyright (c) 2016, Philip Xu <pyx@xrefactor.com>
# License: BSD New, see LICENSE for details.
"""Flask-Pure - a Flask extension for Pure.css"""

from flask import Blueprint, Markup, current_app, url_for

__version__ = '0.2'
__all__ = ['Pure']

CDN_PREFIX = 'http://yui.yahooapis.com/pure/0.6.0/'
LINK_TEMPLATE = '<link rel="stylesheet" href="%s.css">'


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
        app.config.setdefault('PURECSS_RESPONSIVE_GRIDS', True)
        app.config.setdefault('PURECSS_USE_CDN', True)
        app.config.setdefault('PURECSS_USE_MINIFIED', True)

        pure = Blueprint(
            'pure',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=app.static_url_path + '/pure/css')

        app.register_blueprint(pure)

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions['pure'] = self
        app.context_processor(lambda: {'pure': self})

    @property
    def css(self):
        """property the will be rendered as Pure.css :code:`<link>` tags"""
        stylesheets = ['pure']

        if current_app.config['PURECSS_RESPONSIVE_GRIDS']:
            stylesheets.append('grids-responsive')

        if current_app.config['PURECSS_USE_MINIFIED']:
            stylesheets = [ss + '-min' for ss in stylesheets]

        if current_app.config['PURECSS_USE_CDN']:
            stylesheets = [CDN_PREFIX + ss for ss in stylesheets]
        else:
            stylesheets = [
                url_for('pure.static', filename=ss) for ss in stylesheets]

        return Markup('\n'.join(LINK_TEMPLATE % ss for ss in stylesheets))
