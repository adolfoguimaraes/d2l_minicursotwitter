from flask import Flask, jsonify
from flask import render_template
from db.database import db_session
from db.models import Usuarios, Termos, Hashtags, UsuariosCitados, BigramTrigram

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

    query_A = Hashtags.query.filter_by(hashtag="#teamsuperman").first()
    query_B = Hashtags.query.filter_by(hashtag="#teambatman").first()

    total_A = float(query_A.frequencia)
    total_B = float(query_B.frequencia)

    total = total_A + total_B

    percent_A = (total_A / total) * 100
    percent_B = (total_B / total) * 100

    print total, total_A, total_B, percent_A, percent_B

    return render_template("index.html",termos=termos,hashtags=hashtags,usuarios=usuarios,usuarios_citados=usuarios_citados, total=(percent_A, percent_B), bigram_trigram=bigram_trigram, context=context)

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