from flask import Blueprint

routes = Blueprint('routes', __name__)

from .gradlew import *
from .create import *
from .update import *
from .setup import *
from .file import *