import twitter
import os
import redis

# Load environment variables
consumer_key = os.environ.get('TWITTAGOTCHI_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTAGOTCHI_CONSUMER_SECRET')
access_token = os.environ.get('TWITTAGOTCHI_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTAGOTCHI_ACCESS_TOKEN_SECRET')

# Redis Init
# redis_url = os.getenv('TWITTAGOTCHI_REDISTOGO_URL', 'redis://localhost:6379')
# r = redis.from_url(redis_url)

# Twitter Init
api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

api.PostUpdate("Testing")
