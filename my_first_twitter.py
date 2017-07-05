import twitter
import ConfigParser
import os

cfg = ConfigParser.ConfigParser()
cfg.read(os.path.expanduser('~/.twitter/twitter.cfg'))
consumer_key = cfg.get("DEFAULT", 'consumer_key')
consumer_secret = cfg.get("DEFAULT", 'consumer_secret')
access_token_key = cfg.get("DEFAULT", 'access_token_key')
access_token_secret = cfg.get("DEFAULT", 'access_token_secret')

api = twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret)

search_results = api.GetSearch(term="computing")

for status in search_results:
    print status.AsJsonString()

