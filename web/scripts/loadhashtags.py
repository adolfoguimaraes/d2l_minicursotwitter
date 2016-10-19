import os
import sys
import csv

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)

from db.models import  Tweets
from collections import Counter

from nltk.tokenize import regexp_tokenize

tweets = Tweets.query.all()

pattern = r'(https://[^"\' ]+|www.[^"\' ]+|http://[^"\' ]+|\w+|\@\w+|\#\w+)'

dict = {}

for t in tweets:
    local_patterns = regexp_tokenize(t.text.lower(), pattern)

    hashtags = [e for e in local_patterns if e[0] == '#']

    str_date = str(t.date).split(" ")[0].replace("-", "")


    if str_date in dict.keys():
        dict[str_date] += hashtags
    else:
        dict[str_date] = hashtags


with open('../static/js/graph/hashtags.csv', 'w') as csvfile:
    fieldnames = ['hashtag', 'date','count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=",")
    writer.writeheader()

    for d in sorted(dict):
        dict[d] = [w for w in dict[d] if w in ['#teamsuperman','#teambatman','#teamironman','#teamcap']]
        dict_counter = Counter(dict[d])
        writer.writerow({'hashtag': '#teamsuperman', 'date': d, 'count':dict_counter['#teamsuperman']})
        writer.writerow({'hashtag': '#teambatman', 'date': d, 'count': dict_counter['#teambatman']})
        writer.writerow({'hashtag': '#teamironman', 'date': d, 'count': dict_counter['#teamironman']})
        writer.writerow({'hashtag': '#teamcap', 'date': d, 'count': dict_counter['#teamcap']})
