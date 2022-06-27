from urllib import request
from flask import *
import requests
import json

app = Flask(__name__)

config = None;

with open('json/config.json') as f:
   config = json.load(f)

def exchange_code(code):
  data = {
    'client_id': config["Discord"]["ClientId"],
    'client_secret': config["Discord"]["ClientSecret"],
    'grant_type': 'authorization_code',
    'code': str(code),
    'redirect_uri': config["Discord"]["AccessTokenRedirectUri"],
  }

  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }

  print(data)

  r = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
  #r.raise_for_status()

  return r.json()

def getDiscordData(access_token, token_type):
  headers = {
    'Authorization': f"{token_type} {access_token}"
  }

  r = requests.get("https://discord.com/api/users/@me", headers=headers)
  #r.raise_for_status()

  return r.json()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html", oauth_uri=config["Discord"]["OAuth2Uri"])

@app.route('/oauth')
def callback():
    args = request.args
    code = args.get("code")
    data = exchange_code(code)

    resp = make_response(redirect("http://localhost:8080/dashboard"))

    resp.set_cookie("access_token", data["access_token"], max_age=int(data["expires_in"]))
    resp.set_cookie("token_type", data["token_type"], max_age=int(data["expires_in"]))
    resp.set_cookie("refresh_token", data["refresh_token"], max_age=int(data["expires_in"]))
    resp.set_cookie("scope", data["scope"], max_age=int(data["expires_in"]))

    resp.set_cookie("discord_data", json.dumps(getDiscordData(data["access_token"], data["token_type"])), max_age=int(data["expires_in"]))

    return resp

@app.route('/dashboard')
def dashboard():
    if not request.cookies.get("access_token"):
      return (jsonify(error="Unauthorized"), 400)

    discord = json.loads(request.cookies.get("discord_data"))

    discord_id = discord["id"]
    discord_username = discord["username"]
    discord_avatar = discord["avatar"]
    discord_avatar_decoration = discord["avatar_decoration"]
    discord_discriminator = discord["discriminator"]
    discord_public_flags = discord["public_flags"]
    discord_flags = discord["flags"]
    discord_banner = discord["banner"]
    discord_banner_color = discord["banner_color"]
    discord_accent_color = discord["accent_color"]
    discord_locale = discord["locale"]
    discord_mfa_enabled = discord["mfa_eanbled"]
    
    resp = make_response(render_template("dashboard.html", ))

    return resp

def main():
    try:
        app.run(host="0.0.0.0", port="8080", debug=False)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
