from flask import request, jsonify
from . import routes
import base64
import os

@routes.route('/upload/java', methods=['GET', 'POST'])
def file():

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
        package = request.json.get("path")
        
        if os.path.exists(os.path.join(os.getcwd(), "stored", clientIdentification)):

            if request.files:

                file = request.files["file"]
                
                if file.filename.split(".")[1] == "java":
                    
                    javaPath = os.path.join(os.getcwd(), "stored", clientIdentification, "src", "main", "java")
                    path = os.path.join(javaPath, package.replace(".", os.path.sep), file.filename)

                    file.save(path)

        else:
            return (jsonify(error="Bad Request"), 400)


    else:

        return (jsonify(error="Bad Request"), 400)

    return jsonify(success=True)    
