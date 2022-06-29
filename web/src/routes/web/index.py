from . import routes
from flask import *

@routes.route('/')
def index():
  return render_template("index.html", login_uri="http://localhost:8080/login")