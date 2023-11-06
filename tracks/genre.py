from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from tracks.db import get_db

bp = Blueprint('genre', __name__, url_prefix="/genre")

@bp.route('/')
def index():
    db = get_db()
    generos = db.execute(
        'SELECT name as generos, genreId FROM genres'
    ).fetchall()
    return render_template('genre/index.html', generos=generos)

@bp.route('/<int:id>')
def detalle(id):
    db = get_db()
    canciones_g = db.execute(
        """SELECT t.name as cancion,t.trackid,t.Composer as composer FROM tracks t JOIN genres g ON t.Genreid = g.Genreid
            WHERE  g.Genreid = ?""",
        (id,)
    ).fetchall()

    genero = db.execute(
        """SELECT name FROM genres WHERE  genreid = ?""",
        (id,)
    ).fetchone()
    
    return render_template('genre/detalle.html', canciones_g=canciones_g, genero=genero)

