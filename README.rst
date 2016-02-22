===========================================
Flask-Pure - a Flask extension for Pure.css
===========================================

Flask-Pure is an extension to `Flask`_ that helps integrate `Pure.css`_ to your
Flask application.


.. _Flask: http://flask.pocoo.org/
.. _Pure.css: http://purecss.io/


Quick Start
===========


0. Installation

  .. code-block:: sh

    pip install Flask-Pure


1. Configuration

  .. code-block:: python

    from flask import Flask, render_template
    from flask.ext.pure import Pure

    app = Flask(__name__)
    app.config['PURECSS_USE_CDN'] = True
    app.config['PURECSS_USE_MINIFIED'] = True
    Pure(app)

    @app.route('/')
    def hello():
        return render_template('hello.html')

    if __name__ == '__main__':
        app.run(debug=True)


2. In :code:`templates/hello.html`:

  .. code-block:: jinja

    {% extends "pure/layout.html" %}
    {% block title %}Hello world from flask-pure{% endblock %}

    {% block nav %}
    <div class="pure-menu pure-menu-horizontal">
      <!-- ... -->
    </div>
    {% endblock %}

    {% block content %}
      <h1>Hello world</h1>
    {% endblock %}


3. Profit!


License
=======

BSD New, see LICENSE for details.


Links
=====

- `Documentation <http://flask-pure.readthedocs.org/>`_

- `Issue Tracker <https://github.com/pyx/flask-pure/issues/>`_

- `Source Package @ PyPI <https://pypi.python.org/pypi/Flask-Pure/>`_

- `Mercurial Repository @ bitbucket
  <https://bitbucket.org/pyx/flask-pure/>`_

- `Git Repository @ Github
  <https://github.com/pyx/flask-pure/>`_

- `Git Repository @ Gitlab
  <https://gitlab.com/pyx/flask-pure/>`_

- `Development Version
  <http://github.com/pyx/flask-pure/zipball/master#egg=Flask-Pure-dev>`_
