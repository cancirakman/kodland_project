from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

@app.route('/Nedenler')
def nedenler():
    return render_template('reasons.html')

@app.route('/Onlemler')
def onlemler():
    return render_template('precautions.html')

@app.route('/Sonuclar')
def sonuclar():
    return render_template('results.html')

@app.route('/Bilgiler')
def bilgiler():
    return render_template('informations.html')

@app.route('/Form')
def form():
    return render_template('test.html')

@app.route('/Goruntu-Siniflandirma')
def goruntu_siniflandirma():
    return render_template('tm.html')

if __name__ == '__main__':
    app.run(debug=True)
