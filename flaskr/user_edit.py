from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('user_edit', __name__)


@bp.route('/user_update/<int:user_id>', methods=['POST'])
#@bp.route('/user_update2', methods=['POST'])
def edit_user2(user_id):
    db = get_db()
    db.execute(
        'UPDATE user SET user_name = ?, user_firstname = ?, user_lastname = ?, user_email = ? WHERE user_id = ?',
        [request.form['username'],
         request.form['firstname'],
         request.form['lastname'],
         request.form['email'],
        user_id]
    )
    db.commit()
    return redirect(url_for('admin.index'))