from routes import routes
from flask import *
import base64
import json
import os

def main():
    try:
        app = Flask(__name__)
        app.register_blueprint(routes)
        app.run(host="0.0.0.0", port="443", debug=False)
    except Exception as e:
        print("An error occurred: " + e)

main()

def load(discordId):
    clientIdentification = base64.b64encode(discordId.encode("utf-8"))
    if not os.path.exists(clientIdentification):
        print("[+] Created (" + clientIdentification.decode("utf-8") + ")")
        os.mkdir(clientIdentification.decode("utf-8"))

def updateModInfo(ClientIdentification, Id, Name, Description, Version, LogoFile, Url):

    path =  os.path.join(os.getcwd(), f"{ClientIdentification}", "src", "main", "resources", "mcmod.info")

    with open(path, "w") as f:

        mcModInfo = {"modid":f"{Id}"},{"name":f"{Name}"},{"description":f"{Description}"},{"version":f"{Version}"},{"mcversion":"1.12.2"},{"logoFile":f"{LogoFile}"},{"url":f"{Url}"},{"updateUrl":""},{"authorList":[""]},{"screenshots":""},{"dependencies":""}

        json.dump(mcModInfo, f, indent = 2)

        f.close()

def addMixin(clientIdentification, newMixin):

    path = os.path.join(os.getcwd(), f"{clientIdentification}", "src", "main", "resources", "mixins.json")

    with open(path, "r") as f:

        data = json.load(f)

        mixins = data["mixins"]

        mixins.append(newMixin)

        f.close()

        with open(path, "w") as fp:

            json.dump(data, fp, indent=4)
            f.close()