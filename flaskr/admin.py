from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('admin', __name__)

#Display Data - Dashboard
@bp.route('/admin')
@login_required
def index():
    return render_template('admin/admin.html')

@bp.route('/users_list')
@login_required
def get_users():
    db = get_db()
    users = db.execute(
        'SELECT xuser_id, xuser_username, xuser_firstname, xuser_lastname, xuser_email'
        ' FROM xuser'
    ).fetchall()

    return render_template('admin/user_list.html', users=users)

@bp.route('/user_delete', methods=['POST'])
def delete_user():
    db = get_db()
    db.execute(
        'DELETE FROM xuser WHERE xuser_id = ?', [request.form['user_to_delete']]
    )
    db.commit()
    return redirect(url_for('admin.index'))

#@bp.route('/user_update/<int:user_id>', methods=['POST'])
#@bp.route('/<int:user_id>/user_update', methods=('GET', 'POST'))
#def update_user(user_id):

#    return render_template('admin/user_edit.html', user_id=request.form['user_to_edit'])


def get_user(user_id):
    user = get_db().execute(
        'SELECT xuser_id, xuser_username, xuser_firstname, xuser_lastname, xuser_email'
        ' FROM xuser'
        ' WHERE xuser_id = ?',
        (user_id,)
    ).fetchone()

    return user


@bp.route('/<int:user_id>/user_update', methods=['GET', 'POST'])
@login_required
def update_userInfo(user_id):
    #user_id = request.form['user_to_edit']
    print("AAAAA")
    print(user_id)
    print("AAAAA")
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
                'UPDATE xuser SET xuser_username = ?, xuser_firstname = ?, xuser_lastname = ?, xuser_email = ? WHERE xuser_id = ?',
                [username,
                 firstname,
                 lastname,
                 email,
                 user_id]
            )
            db.commit()
            return redirect(url_for('admin.index'))

    return render_template('admin/user_edit.html', user=user)