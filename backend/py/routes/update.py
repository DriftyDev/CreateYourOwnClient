from flask import request, jsonify

from . import routes
import base64
import json
import os


@routes.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == "POST":

        # Discord Id
        discordId = request.json.get("discordId")
        clientIdentification = base64.b64encode(discordId.encode("UTF-8"))

        # API Token
        token = request.json.get("apiToken")

        # TODO: Prevent request flooding
        ip = request.remote_addr

        # Update Method
        method = request.json.get("method")

        if token != ("TEVVWF9JU19SQVRURUQ"): # Base64 'LEUX_IS_RATTED'

            return (jsonify(error="Unauthorized"), 400)

        if method == "MOD_INFO":

            # Args
            id = request.json.get("id")
            name = request.json.get("name")
            description = request.json.get("description")
            version = request.json.get("version")
            logoFile = request.json.get("logoFile")
            url = request.json.get("url")    

            if os.path.exists(clientIdentification):
                
                path = os.path.join(os.getcwd(), "stored", clientIdentification.decode("UTF-8"))

                resourcesPath = os.path.join(path, "src", "main", "resources")

                with open(os.path.join(resourcesPath, "mcmod.info"), "w") as f:

                    modInfo = {"modid":f"{id}"}, {"name":f"{name}"}, {"description":f"{description}"}, {"version":f"{version}"}, {"mcversion":"1.12.2"}, {"logoFile":f"{logoFile}"}, {"url":f"{url}"}, {"updateUrl":""}, {"authorList":[""]}, {"screenshots":""}, {"dependencies":""}

                    json.dump(modInfo, f, indent = 2)

                    f.close()

        elif method == "MIXINS":

            # Args
            newMixin = request.json.get("mixin")

            path = os.path.join(os.getcwd(), clientIdentification.decode("UTF-8"))

            resourcesPath = os.path.join(path, "src", "main", "resources")

            if os.path.exists(clientIdentification):
                with open(os.path.join(resourcesPath, "mixins.json"), "r") as f:

                    data = json.load(f)

                    mixins = data["mixins"]

                    mixins.append(newMixin)

                    f.close()

                    with open(os.path.join(resourcesPath, "mixins.json"), "w") as fp:

                        json.dump(data, fp, indent=4)

                        f.close()

        else:

            return (jsonify(error="Bad Request"), 400)

    else:
        return (jsonify(error="Bad Request"), 400)

    return jsonify(success=True)