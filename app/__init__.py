from app.routes import home
from flask import Flask
def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='p20y20t3h14-news'
  )

  @app.route('/testing')
  def testing():
    return 'Testing App'
  
  # register routes
  app.register_blueprint(home)
  
  return app