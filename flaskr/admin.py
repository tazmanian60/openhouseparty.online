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
        'SELECT user_id, user_name'
        ' FROM user'
    ).fetchall()

    return  render_template('admin/user_list.html', users=users)

@bp.route('/user_delete', methods=['POST'])
def delete_user():
    db = get_db()
    db.execute(
        'DELETE FROM user WHERE user_id = ?',[request.form['user_to_delete']]
    )
    db.commit()
    return redirect(url_for('admin.index'))