from . import routes
from . import config
from flask import *
import requests

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

@routes.route('/oauth2')
def callback():
  args = request.args
  code = args.get("code")
  data = exchange_code(code)

  resp = make_response(redirect("http://localhost:8080/panel"))

  resp.set_cookie("access_token", data["access_token"], max_age=int(data["expires_in"]))
  resp.set_cookie("token_type", data["token_type"], max_age=int(data["expires_in"]))
  resp.set_cookie("refresh_token", data["refresh_token"], max_age=int(data["expires_in"]))
  resp.set_cookie("scope", data["scope"], max_age=int(data["expires_in"]))

  resp.set_cookie("discord_data", json.dumps(getDiscordData(data["access_token"], data["token_type"])), max_age=int(data["expires_in"]))

  return resp