#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_pure import Pure

app = Flask(__name__)

# Including the responsive grids module, this is the default value
app.config['PURECSS_RESPONSIVE_GRIDS'] = True

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
