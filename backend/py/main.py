import json
import os

def UpdateModInfo(Id, Name, Description, Version, LogoFile, Url):
    Path =  os.path.join(os.getcwd(), "base", "src", "main", "resources", "mcmod.info")
    with open(Path, "r") as f:
        
        f.close()
        with open(Path, "w") as fw:

            McModInfo = {"modid":f"{Id}"},{"name":f"{Name}"},{"description":f"{Description}"},{"version":f"{Version}"},{"mcversion":"1.12.2"},{"logoFile":f"{LogoFile}"},{"url":f"{Url}"},{"updateUrl":""},{"authorList":[""]},{"screenshots":""},{"dependencies":""}

            json.dump(McModInfo, fw, indent = 2)
            fw.close()

def addMixin():
    with open("") as f:
        f.read()

UpdateModInfo("abyss", "Abyss", "get good", "1.0", "", "")