var apiToken = "TEVVWF9JU19SQVRURUQ";

function getDiscordId() {
    return "";
}

function updateModInfo(modId, modName, modDescription, modVersion, modLogoFile, modUrl) {
    var json = {
        discordId: getDiscordId(),
        apiToken: apiToken,
        method: "MOD_INFO",
        id: modId,
        name: modName,
        description: modDescription,
        version: modVersion,
        logoFile: modLogoFile,
        url: modUrl
    };

    $.ajax({
        type: 'POST',
        url: 'https://api.mcclientcreator.org/update',
        data: json
    });
}

function addMixin(newMixin) {
    var json = {
        discordId: getDiscordId(),
        apiToken: apiToken,
        method: "MIXINS",
        mixin: newMixin
    };

    $.ajax({
        type: 'POST',
        url: 'https://api.mcclientcreator.org/update',
        data: json
    });
}
