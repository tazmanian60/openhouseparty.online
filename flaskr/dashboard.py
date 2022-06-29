
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('dashboard', __name__)

#Display Data - Dashboard
@bp.route('/')
def index():
    return render_template('dashboard.html')