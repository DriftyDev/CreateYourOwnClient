var apiToken = "TEVVWF9JU19SQVRURUQ";

function getDiscordId() {
    return "";
}

function updateModInfo(modId, modName, modDescription, modVersion, modLogoFile, modUrl) {
    var request = $.post("https://api.mcclientcreator.org/update", {
        discordId: getDiscordId(),
        apiToken: apiToken,
        method: "MOD_INFO",
        id: modId,
        name: modName,
        description: modDescription,
        version: modVersion,
        logoFile: modLogoFile,
        url: modUrl
    })
}

function addMixin(newMixin) {
    var request = $.post("https://api.mcclientcreator.org/update", {
        discordId: getDiscordId(),
        apiToken: apiToken,
        method: "MIXINS",
        mixin: newMixin
    })
}
