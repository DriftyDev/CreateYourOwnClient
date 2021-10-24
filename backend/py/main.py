import json
import os

def UpdateModInfo(Id, Name, Description, Version, McVersion, LogoFile, Url, Screenshots, Dependencies):
    Path =  os.path.join(os.getcwd(), "base", "src", "main", "resources", "mcmod.info")
    with open(Path, "r") as f:
        Raw = json.load(f)
        McModInfo = dict(Raw)
        f.close()
        with open(Path, "w") as fw:
            McModInfo.update({"modid":f"{Id}"})
            McModInfo.update({"name":f"{Name}"})
            McModInfo.update({"description":f"{Description}"})
            McModInfo.update({"version":f"{Version}"})
            McModInfo.update({"mcversion":f"{McVersion}"})
            McModInfo.update({"logoFile":f"{LogoFile}"})
            McModInfo.update({"url":f"{Url}"})
            McModInfo.update({"updateUrl":""})
            McModInfo.update({"authorList":""})
            McModInfo.update({"screenshots":f"{Screenshots}"})
            McModInfo.update({"dependencies":f"{Dependencies}"})
            json.dump(McModInfo, fw, indent = 2)
            fw.close()

def addMixin():
    with open("") as f:
        f.read()

UpdateModInfo("abyss", "Abyss", "get good", "1.0", "1.12.2", "", "", "", "")        


