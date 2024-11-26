from flask import Flask, render_template, request, redirect, url_for
#configurazione del DB
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#configurazione
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)
#crea il db se non esiste 
with app.app_context():
    db.create_all()

lista_spesa = ["casa", "macchina", "zio pera"]
@app.route('/')
def home():
    ListaSpesa.query.all()
    return render_template('index.html', lista=lista_spesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)