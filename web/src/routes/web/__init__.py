from flask import Blueprint
import requests
import json

routes = Blueprint('routes', __name__)

from .oauth2 import *
from .index import *
from .login import *
from .panel import *

config = json.load(open('.../json/config.json'))