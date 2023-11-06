from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from tracks.db import get_db

bp = Blueprint('artist', __name__, url_prefix="/artist")

@bp.route('/')
def index():
    db = get_db()
    artistas = db.execute(
        'SELECT name as artistas FROM artists'
    ).fetchall()
    return render_template('artist/index.html', artistas=artistas)
