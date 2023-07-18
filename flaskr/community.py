
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('community', __name__)

#Display Data - Dashboard
@bp.route('/community')
def index():
    return render_template('community.html')