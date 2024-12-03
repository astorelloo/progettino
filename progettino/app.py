#si importano tutte le cose necessarie
from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from moduls import db, ListaSpesa
app = Flask(__name__)
#si configura sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#si inizializza il db e lo si crea se non ce
db.init_app(app)
with app.app_context():
    db.create_all()

lista_spese = []
#route di default
@app.route('/')
def home():
    #metodo che ci carica la pagina
    lista_spesa = ListaSpesa.query.all()
    return render_template('index.html' , lista_spese = lista_spesa)
#metodo e route per aggiungere gli oggetti al db e lista     
@app.route('/add', methods=['POST'])
def add():
    elemento = request.form['elemento']
    if elemento:
        nuovo_elemento = ListaSpesa(elemento=elemento)
        db.session.add(nuovo_elemento) 
        db.session.commit() 
    return redirect(url_for('home'))
#metodo e route per rimouvere gli oggetti al db e lista 
@app.route('/remove/<int:indice>', methods=['POST'])
def remove(indice):
    elemento = ListaSpesa.query.get_or_404(indice)
    db.session.delete(elemento)
    db.session.commit() 
    return redirect(url_for('home'))
#metodo e route per azzerare gli oggetti al db e lista 
@app.route('/delete', methods=['POST'])
def delete():
    ListaSpesa.query.delete() 
    db.session.commit() 
    return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True)