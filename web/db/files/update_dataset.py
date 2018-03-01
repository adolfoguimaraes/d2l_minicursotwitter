#coding=utf-8
'''

    A simple script to collect tweets by ids.

    Replace the values in consumer_key, consumer_secret, access_token, access_token_secret

    @TODO: Implement more complete script: (1) avoid limit rate, (2) stop and restart script where the script stop (in case of error)

'''

import csv
import time
import sys
import os
import pytz

from twython import Twython
from twython.exceptions import TwythonError, TwythonRateLimitError
from sqlalchemy.exc import IntegrityError
from datetime import datetime

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from models import AllTweets
from database import db_session

# Access app.twitter.com and generate own credentials account.
#Definição das chaves da API do Twitter
consumer_key = None # Get Keys and Access Token at apps.twitter.com
consumer_secret = None # Get Keys and Access Token at apps.twitter.com
access_token = None # Get Keys and Access Token at apps.twitter.com
access_token_secret = None # Get Keys and Access Token at apps.twitter.com

tw = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

result = []
count = 0

with open('tweets_ids.csv', 'rb') as csv_file:
    reader = csv.DictReader(csv_file)
    all_tweets = []
    for row in reader:
        print "Collecting " + str(row['tweet_id'])

        tweet_id = row['tweet_id']

        try:
            tweet = tw.show_status(id=tweet_id)

            t_id = tweet['id']
            t_user = tweet['user']['screen_name']
            t_text = tweet['text']
            t_date = tweet['created_at']
            t_user_image = tweet['user']['profile_image_url']
            t_context = 'bvs'

            fmt = '%Y-%m-%d %H:%M:%S.%f'
            t_date = datetime.strptime(t_date, '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)

            tweet_instance = AllTweets(t_id, t_user, t_text, t_date, t_user_image, t_context)
            db_session.add(tweet_instance)
            db_session.commit()
            count = count + 1
            print("\t " + str(count) + " tweets collected")

        except TwythonRateLimitError as e:
            print "Limit Error. Waiting 15 minutes"
            time.sleep(900)
        except TwythonError as e:
            print("\tERROR: " + str(tweet_id) + " not collected: " + str(e))
        except IntegrityError as e:
            print("\tERROR: " + str(tweet_id) + " not inserted at db: tweet id is already in database")
            db_session.rollback()
        except Exception as e:
            print("\ERROR: " + str(tweet_id + ": " + str(e)))
