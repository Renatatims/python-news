from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

# Home route - renders homepage template
@bp.route('/')
def index():
  # get all posts
  db = get_db()
  posts = (
  db
    .query(Post)
    .order_by(Post.created_at.desc())
    .all()
  )
  return render_template(
  'homepage.html',
  posts=posts
  )

# Login route - renders login template
@bp.route('/login')
def login():
  return render_template('login.html')

# Single Post route - by id
@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')