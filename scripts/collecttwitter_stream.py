#coding=utf-8
#Primeiro precisamos importar o Stramer criado no arquivp "streamingtwitter.py"
from streamingtwitter import MyStreamer

#Em seguida setamos as chaves da API do Twitter
APP_KEY = None # Get Keys and Access Token at apps.twitter.com
APP_SECRET = None # Get Keys and Access Token at apps.twitter.com
OAUTH_TOKEN = None # Get Keys and Access Token at apps.twitter.com
OAUTH_TOKEN_SECRET = None # Get Keys and Access Token at apps.twitter.com

#E criamos nossa instância do coletor
stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#stream.statuses.filter(track="brasil")
stream.statuses.filter(track="brasil", follow="20678688,736392442384154624")