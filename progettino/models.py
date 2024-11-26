#configurazione del DB
from flask_sqlalchemy import flask_sqlalchemy
app = Flask(__name__)

#configurazione
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)
#crea il db se non esiste 
with app.app_context():
    db.create_all()
#______________________________
#creazione della tabella con le colonne
db = SQLAlchemy() #inizialliziamo sqlAlchemy
class ListaSpesa(db.Model):#tabella
    id = db.Column(db.Integer, primary_key=True) #id unico  
    elemento = db.Column(db.String(100), nullable=False) #elemento non nullo