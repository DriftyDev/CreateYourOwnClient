from flask import Blueprint

routes = Blueprint('routes', __name__)

from .create import *
from .update import *