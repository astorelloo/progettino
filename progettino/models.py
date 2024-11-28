from flask_sqlalchemy import SQLAlchemy
#creazione della tabella con le colonne
db = SQLAlchemy() #inizialliziamo sqlAlchemy
class ListaSpesa(db.Model):#tabella
    id = db.Column(db.Integer, primary_key=True) #id unico  
    elemento = db.Column(db.String(100), nullable=False) #elemento non nullo