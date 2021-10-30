from flask import request, jsonify
from . import routes
import base64
import json
import os

@routes.route('/create', methods=['GET', 'POST'])
def main():

    if request.method == "POST":

        # Discord Id
        discordId = request.json.get("id")
        clientIdentification = base64.b64encode(discordId.encode("UTF-8"))

        # API Token
        token = request.json.get("token")

        # TODO: Prevent request flooding
        ip = request.remote_addr

        if token != ("TEVVWF9JU19SQVRURUQ"): # Base64 'LEUX_IS_RATTED'

            return (jsonify(error="Unauthorized"), 400)

        if not os.path.exists(clientIdentification):

            path = clientIdentification.decode("utf-8")

            os.mkdir(path)
            defaultJavaPath = os.path.join("default", "src", "main", "resources")
            defaultResourcesPath = os.path.join("default", "src", "main", "resources")

            javaPath = os.mkdir(os.path.join(path, "src", "main", "java"))
            resourcesPath = os.mkdir(os.path.join(path, "src", "main", "resources"))

            f = open(os.path.join(defaultResourcesPath, "mcmod.info"))
            modInfoDefault = f.read()

            with open(os.path.join(resourcesPath, "mcmod.info"), "w") as f:

                json.dump(modInfoDefault, f, indent=2)

                f.close()

            f = open(os.path.join(defaultResourcesPath, "mixins.json"))
            mixinsDefault = f.read

            with open(os.path.join(resourcesPath, "mixins.json"), "w") as f:

                json.dump(mixinsDefault, f, indent=4)

                f.close()




    else:

        return  (jsonify(error="Bad Request"), 400)



    return jsonify(success=True)
