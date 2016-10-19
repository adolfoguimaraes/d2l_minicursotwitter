#coding=utf-8
#Primeiro precisamos importar o Stramer criado no arquivp "streamingtwitter.py"
from streamingtwitter import MyStreamer

#Em seguida setamos as chaves da API do Twitter
APP_KEY = "0rBTp9a35qIvA5ufGpxPGNkWu"
APP_SECRET = "rGStqnwrDjuzo1zwnXjpPlrilvDmvNljhRh6cTs1pG48K6ZLG6"
OAUTH_TOKEN = "736392442384154624-blYbsB4awwSezrNUH7L5jTG6JPglJy3"
OAUTH_TOKEN_SECRET = "bvPr7Y8BQeyN46UKZtDJPyP0Bx4Y8IuDRDVYxsc3LNAlb"

#E criamos nossa instância do coletor
stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#stream.statuses.filter(track="brasil")
stream.statuses.filter(track="brasil", follow="20678688,736392442384154624")