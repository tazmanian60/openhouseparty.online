
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('contact_us', __name__)

#Display Data - About
@bp.route('/contact_us')
def index():
    return render_template('contact_us.html')