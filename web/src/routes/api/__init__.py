from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from .gradlew import *
from .update import *
from .file import *
from .new import *