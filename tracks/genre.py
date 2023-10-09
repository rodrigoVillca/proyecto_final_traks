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
        'SELECT name FROM genres'
    ).fetchall()
    return render_template('genre/index.html', generos=generos)

