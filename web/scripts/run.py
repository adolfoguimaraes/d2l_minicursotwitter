from collecting import Collecting
from processing import Processing

import sys
import os
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)

from db.models import  UsuariosCitados, Usuarios, Hashtags, Termos, BigramTrigram
from db.database import  db_session
collector = Collecting()
processor = Processing()


def start(context, collect):

    if collect:
        print("Coletando Twitters")
        collector.collect("brasil", 5, 10, 2, context)

    print
    print("Processando Twitters")
    list_texts, list_user = collector.get_tweets_from_database(context)
    final_words = processor.get_final_words(list_texts, False)
    frequence_terms = processor.get_frequence_terms(final_words)
    frequence_users = processor.get_frequence_users(list_user)
    frequence_users_cited = processor.get_frequence_users_cited()
    frequence_hashtags = processor.get_frequence_hashtags()
    bigrams, trigrams = processor.get_bigrams_trigrams(final_words)
    objects = []
    # deletando dados da tabela
    try:
        num_rows_deleted = db_session.query(BigramTrigram).delete()
        db_session.commit()
    except:
        db_session.rollback()
    try:
        num_rows_deleted = db_session.query(Usuarios).delete()
        db_session.commit()
    except:
        db_session.rollback()
    try:
        num_rows_deleted = db_session.query(Hashtags).delete()
        db_session.commit()
    except:
        db_session.rollback()
    try:
        num_rows_deleted = db_session.query(UsuariosCitados).delete()
        db_session.commit()
    except:
        db_session.rollback()
    try:
        num_rows_deleted = db_session.query(Termos).delete()
        db_session.commit()
    except:
        db_session.rollback()
    for t in frequence_terms:
        new_ = Termos(t[0], t[1])

        db_session.add(new_)
        db_session.commit()
    for t in frequence_users:
        new_ = Usuarios(t[0], t[1])

        db_session.add(new_)
        db_session.commit()
    for t in frequence_users_cited:
        new_ = UsuariosCitados(t[0], t[1])

        db_session.add(new_)
        db_session.commit()
    for t in frequence_hashtags:
        new_ = Hashtags(t[0], t[1])

        db_session.add(new_)
        db_session.commit()
    for b in bigrams:
        text = ' '.join(word for word in b)

        new_ = BigramTrigram(text, 0)

        db_session.add(new_)
        db_session.commit()
    for t in trigrams:
        text = ' '.join(word for word in t)

        new_ = BigramTrigram(text, 1)

        db_session.add(new_)
        db_session.commit()


if __name__ == "__mmain__":

    context = 'bvs'
    collect = False

    start(context, collect)