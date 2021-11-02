from flask import request, jsonify
from . import routes
import base64
import os

@routes.route('/gradlew/build', methods=['GET', 'POST'])
def build():

    if request.method == "POST":

        # Discord Id
        discordId = request.json.get("discordId")
        clientIdentification = base64.b64encode(discordId.encode("UTF-8"))

        # API Token
        token = request.json.get("apiToken")

        # TODO: Prevent request flooding
        ip = request.remote_addr

        if token != ("TEVVWF9JU19SQVRURUQ"): # Base64 'LEUX_IS_RATTED'

            return (jsonify(error="Unauthorized"), 400)

        path = os.path.join(os.getcwd(), "stored", clientIdentification.decode("UTF-8"))
        defaultPath = os.path.join(os.getcwd(), "default")
        gradlew = os.path.join(defaultPath, "gradlew")

        os.system(f"cd {path}; ./{gradlew} build")

    return jsonify(success=True)          

        