from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db

# Dashboard routes
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# /dashboard
@bp.route('/')
def dash():
  # User's posts are displayed in the dashboard
  db = get_db()
  posts = (
    db.query(Post)
    .filter(Post.user_id == session.get('user_id'))
    .order_by(Post.created_at.desc())
    .all()
  )
  return render_template(
    'dashboard.html',
    posts=posts,
    loggedIn=session.get('loggedIn')
  )

# /dashboard/edit/<id>
@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')