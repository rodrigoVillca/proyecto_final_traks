from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from tracks.db import get_db

bp = Blueprint('tracks', __name__, url_prefix="/tracks")

@bp.route('/')
def index():
    db = get_db()
    canciones = db.execute(
        'SELECT Name AS canciones FROM tracks'
    ).fetchall()
    return render_template('track/index.html', canciones=canciones)
