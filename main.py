import os
import json
import argparse
import oauth2 as oauth

parser = argparse.ArgumentParser(
    description = 'DISCOVER TWITTER | Get followers list of user'
)

parser.add_argument(
    'screen_name',
    metavar = 'screen_name',
    type    = str,
    nargs   = '+',
    help    = 'twitter screen_name'
)

CONSUMER_KEY    = os.environ.get("CONSUMER_KEY", None)
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET", None)

ACCESS_TOKEN        = os.environ.get("ACCESS_TOKEN", None)
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET", None)

consumer        = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token    = oauth.Token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)
client          = oauth.Client(consumer, access_token)

args = parser.parse_args()

endpoint_URL = "https://api.twitter.com/1.1/followers/list.json" \
    "?cursor=-1" \
    "&screen_name=" + args.screen_name[0] + \
    "&skip_status=true" \
    "&include_user_entities=false"

response, data = client.request(endpoint_URL)

with open('output/' + args.screen_name[0] + '.json', 'w') as outfile:
    json.dump(json.loads(data), outfile, indent=4)
