#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask.ext.pure import Pure

app = Flask(__name__)

# Using external CDN links, this is the default value
app.config['PURECSS_USE_CDN'] = True

# Serving minified version, this is the default value
app.config['PURECSS_USE_MINIFIED'] = True

Pure(app)


@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
