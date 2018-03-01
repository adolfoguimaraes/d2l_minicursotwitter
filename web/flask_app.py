from flask import Flask, jsonify
from flask import render_template
from db.database import db_session
from db.models import Usuarios, Termos, Hashtags, HashtagsGraph, UsuariosCitados, BigramTrigram

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def load_from_db(limit=10):

    query_usuarios = Usuarios.query.order_by(Usuarios.frequencia.desc()).limit(limit).all()
    query_termos = Termos.query.order_by(Termos.frequencia.desc()).limit(limit).all()
    query_hashtags = Hashtags.query.order_by(Hashtags.frequencia.desc()).limit(limit).all()
    query_usuarios_citados = UsuariosCitados.query.order_by(UsuariosCitados.frequencia.desc()).limit(limit).all()

    query_bigram_trigram = BigramTrigram.query.all()

    return query_termos, query_hashtags, query_usuarios, query_usuarios_citados, query_bigram_trigram

@app.route("/")
def home():

    context = 'bvs'

    termos, hashtags, usuarios, usuarios_citados, bigram_trigram = load_from_db(10)

    query_a = Hashtags.query.filter_by(hashtag="#teamsuperman").first()
    query_b = Hashtags.query.filter_by(hashtag="#teambatman").first()

    total_a = 0
    total_b = 0
    percent_a = 0
    percent_b = 0
    total = 0

    if query_a and query_b:
        total_a = float(query_a.frequencia)
        total_b = float(query_b.frequencia)

        total = total_a + total_b

        percent_a = (total_a / total) * 100
        percent_b = (total_b / total) * 100

    return render_template("index.html",termos=termos,hashtags=hashtags,usuarios=usuarios,usuarios_citados=usuarios_citados, total=(percent_a, percent_b), bigram_trigram=bigram_trigram, context=context)


@app.route("/graph/")
def graph():

    query_hashtag = HashtagsGraph.query.filter_by(context="bvs").all()
    all_ = []
    for q in query_hashtag:
        date_ = str(q.date).split(" ")[0]
        t = {}
        t['date'] = date_
        t['count'] = q.frequencia
        t['hashtag'] = q.hashtag
        all_.append(t)

    return jsonify(**{'list': all_})


@app.route("/cloud/")
def cloud():

    query_termos = Termos.query.order_by(Termos.frequencia.desc()).limit(400).all()

    t = {}

    for q in query_termos:
        t[q.termo] = q.frequencia

    return jsonify(**t)


if __name__ == "__main__":
    app.debug = True
    app.run()
