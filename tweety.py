#!/usr/bin/env python

from birdy.twitter import AppClient

try:
    from config import *
except:
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_TOKEN = ''

def fetch_tweet(text):
    client = AppClient(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN)
    response = client.api.search.tweets.get(q = text, count = 100)
    statuses = []
    statuses += response.data.statuses
    status = statuses[1]
    for status in statuses:
        tweet = status.text
        posted_by = '{} ({})'.format(status.user.screen_name, status.user.followers_count)
        occured_at = str(datetime.datetime.strptime(status.created_at, r"%a %b %d %H:%M:%S +0000 %Y"))
        print posted_by + ' at ' + occured_at + 'said: ' + tweet + '\n'    


if __name__ == '__main__':
    from sys import argv
    import datetime
    
    script, query = argv

    if len(argv) > 0:
        text = ' '.join(query)
        fetch_tweet(query)        
    else:
        print "Give tweety a chance honey! (:"
     