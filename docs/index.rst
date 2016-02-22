.. include:: ../README.rst


Configuration
=============

============================ ==================================================
Option                       Description
============================ ==================================================
:code:`PURECSS_USE_CDN`      If :code:`True`, css files will be served from
                             CDN. If :code:`False`, local copies of css files
                             will be served.  Default value is :code:`True`.
:code:`PURECSS_USE_MINIFIED` If :code:`True`, the minified version of css files
                             will be used.  Default value is :code:`True`
============================ ==================================================


Template
========

In addition to provide Pure.css static assets, Flask-Pure comes with
:code:`HTML5` template located in :code:`pure/layout.html` for layout.

==================== =====================================================
Predefined Blocks    Purpose
==================== =====================================================
:code:`html_attribs` :code:`<html>`'s attributes
:code:`head`         all content inside :code:`<head>` and :code:`</head>`
:code:`meta`         for all :code:`<meta>` tags
:code:`title`        content inside :code:`<title>` and :code:`</title>`
:code:`style`        links to css stylesheets
:code:`body_attribs` :code:`<body>`'s attributes
:code:`body`         all content inside :code:`<body>` and :code:`</body>`
:code:`nav`          navigation links
:code:`content`      main content
:code:`script`       embedded javascript
==================== =====================================================


API
===

.. automodule:: flask_pure
  :members:
