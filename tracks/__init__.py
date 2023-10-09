import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # genere enlace de ruta para mostrar mensaje.
    @app.route('/hola')
    def hello():
        return 'Hola, mundo!'
    #importo desde el archivo db la base de datos.
    from . import db, genre, tracks, album, artists
    db.init_app(app)
    app.register_blueprint(genre.bp)
    app.register_blueprint(tracks.bp)
    app.register_blueprint(album.bp)
    app.register_blueprint(artists.bp)

    return app