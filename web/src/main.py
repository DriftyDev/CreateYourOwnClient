from routes.api import api
from routes.web import routes
from urllib import request
from flask import *
import requests
import json

app = Flask(__name__)

def main():
  try:
    app.register_blueprint(api)
    app.register_blueprint(routes)
    app.run(host="0.0.0.0", port="8080", debug=False)
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()
