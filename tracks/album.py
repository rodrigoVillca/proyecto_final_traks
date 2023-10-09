from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from tracks.db import get_db

bp = Blueprint('album', __name__, url_prefix="/album")

@bp.route('/')
def index():
    db = get_db()
    albums = db.execute(
        'SELECT title as albums FROM albums'
    ).fetchall()
    return render_template('album/index.html', albums=albums)

