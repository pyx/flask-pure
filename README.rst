===========================================
Flask-Pure - a Flask extension for Pure.css
===========================================

Flask--Pure adds `Pure.css`_ support to your Flask application.


Quick Start
===========


0. Installation

  .. code-block:: sh

    pip install Flask-Pure


1. In code:

  .. code-block:: python

    from flask.ext.pure import Pure

    ...

    Pure(app)


2. In template:

  .. code-block:: jinja

    {% extends "pure/layout.html" %}
    {% block title %}Hello world from flask-pure{% endblock %}

    {% block navbar %}
    <div class="pure-menu pure-menu-horizontal">
      <!-- ... -->
    </div>
    {% endblock %}

    {% block content %}
      <h1>Hello world</h1>
    {% endblock %}

3. Profit!


Links
=====

* `documentation <http://flask-pure.readthedocs.org/>`_
* `development version
  <http://github.com/pyx/flask-pure/zipball/master#egg=Flask-Pure-dev>`_


.. _Pure.css: http://purecss.io/
