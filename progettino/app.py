from flask import Flask, render_template
#render_template: collegare file HTML.


#base per far funzionare flask
app = Flask(__name__)
@app.route('/')
def home():
    render_template('index.html')
#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)