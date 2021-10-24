import json

def UpdateModInfo(Id, Name, Description, Version, McVersion, LogoFile, Url, UpdateUrl, Screenshots, Dependencies):
    Path = "base\\src\\main\\resources\\mcmod.info"
    with open(Path, "r") as f:
        t = f.read()
        McModInfo = json.load(t)
        ModId = McModInfo["modid"]
        ModName = McModInfo["name"]
        ModDescription = McModInfo["descripttion"]
        ModVersion = McModInfo["version"]
        ModMcVersion = McModInfo["mcversion"]
        ModLogoFilePath = McModInfo["logoFile"]
        ModUrl = McModInfo["url"]
        ModUpdateUrl = McModInfo["updateUrl"]
        ModScreenshots = McModInfo["screenshots"]
        ModDependencies = McModInfo["dependencies"]
        f.close()
    with open(Path) as f:
        
        f.close()

def addMixin():
    with open("") as f:
        f.read()


