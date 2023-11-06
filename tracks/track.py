from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from tracks.db import get_db

bp = Blueprint('track', __name__, url_prefix="/track")

@bp.route('/')
def index():
    db = get_db()
    canciones = db.execute(
        'SELECT Name AS canciones, trackId FROM tracks'
    ).fetchall()
    return render_template('track/index.html', canciones=canciones)

@bp.route('/<int:id>')
def detalle(id):
    db = get_db()
    cancion = db.execute(
        """SELECT t.Name AS nombre, t.milliseconds AS duracion, t.Composer  FROM tracks t
        WHERE  t.trackId = ?""",
        (id,)
    ).fetchone()


    return render_template('track/detalle.html', cancion=cancion)
