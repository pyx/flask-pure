.. include:: ../README.rst


Caveat
======

The stylesheet provided by template variable :code:`pure.css` is the 'Rollups'
version with all the modules in Pure. The responsive grids module that included
by default can be turned off explicitly.

Thus, this extension is an 'all-or-nothing' approach, there is no plan to
support selectable modules currently, as it is so trivial to roll your own.

The conditional IE 8/9 hack are not included, please refer to Pure's official
documentation if this is the concern.


Configuration
=============

================================ =============================================
Option                           Description
================================ =============================================
:code:`PURECSS_RESPONSIVE_GRIDS` If :code:`True`, the responsive grids module
                                 will be included as well.  Default value is
                                 :code:`True`
:code:`PURECSS_USE_CDN`          If :code:`True`, css files will be served
                                 from CDN. If :code:`False`, local copies of
                                 css files will be served.  Default value is
                                 :code:`True`
:code:`PURECSS_USE_MINIFIED`     If :code:`True`, the minified version of css
                                 files will be used.  Default value is
                                 :code:`True`
================================ =============================================


Template
========

In addition to providing Pure.css static assets, Flask-Pure comes with HTML5
template located in :code:`pure/layout.html` for layout.

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


Pure.css Version
================

The bundled version of Pure.css is v0.6.0


API
===

.. automodule:: flask_pure
  :members:


Contributors
============

.. include:: ../AUTHORS


Changelog
=========


Version 0.3
-----------

- Switched CDN url to https version (Contributed by Bastian Kuhn)


Version 0.2
-----------

- Added option to turned off the responsive grids module
- Used an instance of extension as namespace instead of a single template
  variable


Version 0.1
-----------

- Initial public release
