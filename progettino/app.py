from flask import Flask
#inizializza l'app Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "primo step va"

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)