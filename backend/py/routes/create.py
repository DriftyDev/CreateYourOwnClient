from flask import request, jsonify
from . import routes
import base64
import json
import os

@routes.route('/create', methods=['GET', 'POST'])
def create():

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

        if not os.path.exists(path):

            os.makedirs(path)
            defaultJavaPath = os.path.join(os.getcwd(), "default", "src", "main", "java")
            defaultResourcesPath = os.path.join(os.getcwd(), "default", "src", "main", "resources")

            javaPath = os.path.join(path, "src", "main", "java")
            os.makedirs(javaPath)

            resourcesPath = os.path.join(path, "src", "main", "resources")
            os.makedirs(resourcesPath)

            f = open(os.path.join(defaultResourcesPath, "mcmod.info"))
            modInfoDefault = json.load(f)

            with open(os.path.join(resourcesPath, "mcmod.info"), "w") as f:

                json.dump(modInfoDefault, f, indent=2)

                f.close()

            f = open(os.path.join(defaultResourcesPath, "mixins.json"))
            mixinsDefault = json.load(f)

            with open(os.path.join(resourcesPath, "mixins.json"), "w") as f:

                json.dump(mixinsDefault, f, indent=4)

                f.close()

    else:

        return (jsonify(error="Bad Request"), 400)



    return jsonify(success=True)
