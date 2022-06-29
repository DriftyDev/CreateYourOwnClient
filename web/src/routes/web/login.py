from . import routes
from . import config
from flask import *

@routes.route('/login')
def login():
  return render_template("login.html", oauth_uri=config["Discord"]["OAuth2Uri"])