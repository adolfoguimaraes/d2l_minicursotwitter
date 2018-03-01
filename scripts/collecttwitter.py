#coding=utf8

#Imports necessários
from twython import Twython
from datetime import datetime

#Definição das chaves da API do Twitter
APP_KEY = None # Get Keys and Access Token at apps.twitter.com
APP_SECRET = None # Get Keys and Access Token at apps.twitter.com
OAUTH_TOKEN = None # Get Keys and Access Token at apps.twitter.com
OAUTH_TOKEN_SECRET = None # Get Keys and Access Token at apps.twitter.com

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