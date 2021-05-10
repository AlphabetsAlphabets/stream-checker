import requests
import json

with open("token.json") as f:
    json = json.load(f)

client_id = json["client_id"]
client_secret = json["client_secret"]

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

"""
https://www.twitch.tv/login?client_id=eop2kevuqig0drrnj9qoknsu9964a0&redirect_param
s=client_id%3Deop2kevuqig0drrnj9qoknsu9964a0%26redirect_uri%3Dhttps%253A%252F%252Fy
jh_result.com%26response_type%3Dtoken%2Bid_token%26scope%3Duser%253Aread%253Afollow
s
"""

