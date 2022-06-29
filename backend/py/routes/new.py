from flask import request, jsonify
from . import routes
import base64
import json
import os

@routes.route('/create', methods=['GET', 'POST'])
def new():

    if request.method == "POST":
        if not request.cookies.get("access_token"): # Base64 'LEUX_IS_RATTED'

            return (jsonify(error="Unauthorized"), 400)

        # Discord Id
        discordId = request.cookies.get("discord")["id"]
        clientIdentification = base64.b64encode(discordId.encode("UTF-8"))

        # Mcmod.info args
        id = request.json.get("id")
        name = request.json.get("name")
        description = request.json.get("description")
        version = request.json.get("version")
        logoFile = request.json.get("logoFile")
        url = request.json.get("url")

        # API Token
        token = request.json.get("apiToken")

        # TODO: Prevent request flooding
        ip = request.remote_addr


        path = os.path.join(os.getcwd(), "stored", clientIdentification.decode("UTF-8"))

        if not os.path.exists(path):

            os.makedirs(path)
            defaultResourcesPath = os.path.join(os.getcwd(), "default", "src", "main", "resources")

            javaPath = os.path.join(path, "src", "main", "java")
            os.makedirs(javaPath)

            resourcesPath = os.path.join(path, "src", "main", "resources")
            os.makedirs(resourcesPath)

            #f = open(os.path.join(defaultResourcesPath, "mcmod.info"))
            #modInfoDefault = json.load(f)

            with open(os.path.join(resourcesPath, "mcmod.info"), "w") as f:

                modInfo = {"modid":f"{id}"}, {"name":f"{name}"}, {"description":f"{description}"}, {"version":f"{version}"}, {"mcversion":"1.12.2"}, {"logoFile":f"{logoFile}"}, {"url":f"{url}"}, {"updateUrl":""}, {"authorList":[""]}, {"screenshots":""}, {"dependencies":""}

                json.dump(modInfo, f, indent=2)

                f.close()

            f = open(os.path.join(defaultResourcesPath, "mixins.json"))
            mixinsDefault = json.load(f)

            with open(os.path.join(resourcesPath, "mixins.json"), "w") as f:

                json.dump(mixinsDefault, f, indent=4)

                f.close()

    else:

        return (jsonify(error="Bad Request"), 400)



    return jsonify(success=True)
