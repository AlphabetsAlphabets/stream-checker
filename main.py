import requests
import json

try:
    with open("token.json") as f:
        json = json.load(f)
        client_id = json["client_id"]
        client_secret = json["client_secret"]
except FileNotFoundError:
    import os
    client_secret = os.environ["CLIENT_SECRET"]
    client_id = os.environ["CLIENT_ID"]


def check_status():
    uri = "https://api.twitch.tv/helix/search/channels?query=a_seagull"
    data = {"client-id": client_id, "Authorization": f"Bearer {client_secret}"}
    r = requests.get(uri, headers=data)
    print(r.json())

# ?client_id=<your client ID> &redirect_uri=<your registered redirect URI>
# &response_type=<type> &scope=<space-separated list of scopes> &claims=<JSON
# object specifying requested claims>"

uri = "https://id.twitch.tv/oauth2/authorize"
redirect_uri = "https://localhost"
 
params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": "user:read:follows"
        }

r = requests.get(uri, params=params)
print(r.url)

