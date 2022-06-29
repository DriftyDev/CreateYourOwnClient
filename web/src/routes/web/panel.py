from . import routes
from flask import *

@routes.route('/panel')
def panel():
  if not request.cookies.get("access_token"):
    return (jsonify(error="Unauthorized"), 400)

  discord = json.loads(request.cookies.get("discord_data"))

  discord_id = discord["id"]
  discord_username = discord["username"]
  discord_avatar = discord["avatar"]
  #discord_avatar_decoration = discord["avatar_decoration"]
  discord_discriminator = discord["discriminator"]
  #discord_public_flags = discord["public_flags"]
  #discord_flags = discord["flags"]
  discord_banner = discord["banner"]
  discord_banner_color = discord["banner_color"]
  #discord_accent_color = discord["accent_color"]
  discord_locale = discord["locale"]
  #discord_mfa_enabled = discord["mfa_eanbled"]

  if request.method == "POST":
    return "yes"

  return render_template("panel.html", discord_id=discord_id, discord_username=discord_username, discord_discriminator=discord_discriminator, discord_avatar=discord_avatar, discord_banner=discord_banner, discord_banner_color=discord_banner_color, discord_locale=discord_locale)