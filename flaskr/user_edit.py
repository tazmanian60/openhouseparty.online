from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('user_edit', __name__)


@bp.route('/<int:user_id>/user_update', methods=['POST'])
#@bp.route('/user_update2', methods=['POST'])
def update_user(user_id):
    user = get_user(user_id)
    if request.method == 'POST':
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        error = None

        if not username:
            error = 'Username is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE xUser SET xUser_username = ?, xUser_firstname = ?, xUser_lastname = ?, xUser_email = ? WHERE xUser_id = ?',
                [username,
                 firstname,
                 lastname,
                 email,
                 user_id]
            )
            db.commit()
            return redirect(url_for('admin.index'))

    return render_template('admin/user_edit.html', user=user)





    #db = get_db()
    #db.execute(
    #    'UPDATE user SET user_name = ?, user_firstname = ?, user_lastname = ?, user_email = ? WHERE user_id = ?',
    #    [request.form['username'],
    #     request.form['firstname'],
    #     request.form['lastname'],
    #     request.form['email'],
    #    user_id]
    #)
    #db.commit()
    #return redirect(url_for('admin.index'))





