import flask

from flask.ext.pure import Pure


def create_client(use_cdn=None, use_minified=None, responsive=None):
    app = flask.Flask(__name__)

    app.config['TESTING'] = True
    if use_cdn is not None:
        app.config['PURECSS_USE_CDN'] = use_cdn
    if use_minified is not None:
        app.config['PURECSS_USE_MINIFIED'] = use_minified
    if responsive is not None:
        app.config['PURECSS_RESPONSIVE_GRIDS'] = responsive

    Pure(app)

    @app.route('/')
    def index():
        return flask.render_template('pure/layout.html')

    return app.test_client()


def test_serve_static_pure_css_files():
    client = create_client()
    response = client.get('/static/pure/css/pure.css')
    assert response.status_code == 200
    response = client.get('/static/pure/css/pure-min.css')
    assert response.status_code == 200


def test_serve_static_grids_css_files():
    client = create_client()
    response = client.get('/static/pure/css/grids-responsive.css')
    assert response.status_code == 200
    response = client.get('/static/pure/css/grids-responsive-min.css')
    assert response.status_code == 200


def test_use_cdn_by_default():
    client = create_client()
    html = client.get('/').data.decode()
    assert '/static/pure/css/pure-min.css' not in html
    assert '/static/pure/css/grids-responsive-min.css' not in html

    client = create_client(use_cdn=False)
    html = client.get('/').data.decode()
    assert '/static/pure/css/pure-min.css' in html
    assert '/static/pure/css/grids-responsive-min.css' in html


def test_use_minified_by_default():
    client = create_client()
    html = client.get('/').data.decode()
    assert 'pure-min.css' in html
    assert 'grids-responsive-min.css' in html

    client = create_client(use_minified=False)
    html = client.get('/').data.decode()
    assert 'pure.css' in html
    assert 'grids-responsive.css' in html


def test_responsive_grids_by_default():
    client = create_client()
    html = client.get('/').data.decode()
    assert 'grids-responsive-min.css' in html

    client = create_client(responsive=False)
    html = client.get('/').data.decode()
    assert 'grids-responsive-min.css' not in html
