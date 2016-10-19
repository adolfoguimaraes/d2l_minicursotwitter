#coding=utf8

#Imports necessários
from twython import Twython
from datetime import datetime

#Definição das chaves da API do Twitter
APP_KEY = "0rBTp9a35qIvA5ufGpxPGNkWu"
APP_SECRET = "rGStqnwrDjuzo1zwnXjpPlrilvDmvNljhRh6cTs1pG48K6ZLG6"
OAUTH_TOKEN = "736392442384154624-blYbsB4awwSezrNUH7L5jTG6JPglJy3"
OAUTH_TOKEN_SECRET = "bvPr7Y8BQeyN46UKZtDJPyP0Bx4Y8IuDRDVYxsc3LNAlb"

#Instanciando o Twython com os parâmetros necessários
tw = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#Relizando uma busca com a palavra **brasil** e imprimindo o resultado
result = tw.search(q="brasil",count=100,lang="pt")
print(result)

#Realizando uma busca com a hashtag #MasterChefBR
result_hashtag = tw.search(q="#MasterChefBR", count=5, lang="pt")

#Realizando uma busca com várias hashtags
result_multi = tw.search(q="#MasterChefBR OR #MasterChef", count=100, lang="pt")

#Imprimindo metadados da busca
print(result_hashtag['search_metadata'])

#Imprimindo os tweets coletados a partir da busca
print(result_hashtag['statuses'])

#Imprimindo id e texto de cada tweet coletado

tweets = result_hashtag['statuses']

for tweet in tweets:
    print(tweet['id'])
    print(tweet['text'])


#Imprimindo informações do usuário de um tweet específico
first_tweet = tweets[0]

user_ = first_tweet['user']

print(user_)

print(user_['id']) #id do usuário
print(user_['name']) #nome do usuário
print(user_['screen_name']) #username do usuário
print(user_['description']) #descrição do perfil
print(user_['profile_image_url']) #url da imagem do perfil

#Coletando e imprimindo a timeline de usuário específico

tw_timeline = tw.get_user_timeline(screen_name="@adolfoguimaraes")

for tweet in tw_timeline:
    print(tweet['text'])

#Buscando informações específica de um usuário

tw_user = tw.show_user(screen_name="@adolfoguimaraes")

print(tw_user['id']) #id do usuário
print(tw_user['name']) #nome do usuário
print(tw_user['screen_name']) #username do usuário
print(tw_user['description']) #descrição do perfil
print(tw_user['profile_image_url']) #url da imagem do perfil