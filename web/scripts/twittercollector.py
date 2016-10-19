import time
import sys
import os
from datetime import datetime
import pytz

from twython import Twython

twitter = None
count = 0
COLLECT = True

class TwitterCollector():

    def __init__(self):

        self.APP_KEY = "0rBTp9a35qIvA5ufGpxPGNkWu"
        self.APP_SECRET = "rGStqnwrDjuzo1zwnXjpPlrilvDmvNljhRh6cTs1pG48K6ZLG6"
        self.OAUTH_TOKEN = "736392442384154624-blYbsB4awwSezrNUH7L5jTG6JPglJy3"
        self.OAUTH_TOKEN_SECRET = "bvPr7Y8BQeyN46UKZtDJPyP0Bx4Y8IuDRDVYxsc3LNAlb"

        self.twitter = Twython(self.APP_KEY, self.APP_SECRET, self.OAUTH_TOKEN, self.OAUTH_TOKEN_SECRET)

    def get_user(self, user_screenname):
        try:
            user = self.twitter.show_user(screen_name=user_screenname)
        except Exception as e:
            user = None

        return user

    def collect(self, query, waiting_time, count, number_of_attempts):

        if query == '':
            return

        last_since = -1

        tweets_collect = []
        list_ids = []

        for i in range(0, number_of_attempts):

            if i == 0:
                results = self.twitter.search(q=query, count=count, lang='pt')
            else:
                results = self.twitter.search(q=query, count=count, lang='pt', since_id=last_since)

            count_control = 0

            for tweet in results['statuses']:

                if count_control == 0:
                    last_since = tweet['id']
                    count_control += 1

                id_tweet = tweet['id']
                user_tweet = tweet['user']
                text_tweet = tweet['text']
                posted_at_tweet = tweet['created_at']

                fmt = '%Y-%m-%d %H:%M:%S.%f'
                new_date = datetime.strptime(posted_at_tweet,'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)

                dict = {
                    'id': id_tweet,
                    'user': user_tweet,
                    'text': text_tweet,
                    'posted_at': datetime.strptime(new_date.strftime(fmt),fmt),
                    'social_media': 't',
                    'type': 'hashtag'
                }


                if id_tweet not in list_ids:
                    tweets_collect.append(dict)
                    list_ids.append(id_tweet)


            #waiting_time in seconds
            time.sleep(waiting_time)


        return tweets_collect
