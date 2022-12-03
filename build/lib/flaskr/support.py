
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('support', __name__)

#Display Data - Support
@bp.route('/support')
def index():
    return render_template('support.html')