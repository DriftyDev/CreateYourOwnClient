from flask import Blueprint

routes = Blueprint('routes', __name__)

from .gradlew import *
from .update import *
from .file import *
from .new import *