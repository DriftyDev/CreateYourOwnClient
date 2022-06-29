from flask import request, jsonify
from . import api
import base64
import os

@api.route('/gradlew', methods=['GET', 'POST'])
def gradlew():

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

        # Args
        action = request.json.get("action")

        if not action:

            return (jsonify(error="Bad Request"), 400)


        path = os.path.join(os.getcwd(), "stored", clientIdentification.decode("UTF-8"))
        defaultPath = os.path.join(os.getcwd(), "default")
        gradlew = os.path.join(defaultPath, "gradlew")

        os.system(f"cd {path}; ./{gradlew} {action}")
    else:
        return (jsonify(error="Bad Request"), 400) 

    return jsonify(success=True)

        