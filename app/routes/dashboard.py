from flask import Blueprint, render_template

# Dashboard routes
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# /dashboard
@bp.route('/')
def dash():
  return render_template('dashboard.html')

# /dashboard/edit/<id>
@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')