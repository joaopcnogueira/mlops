from flask import Flask

app = Flask('meu_app')

@app.route('/')
def home():
    return 'Hello World'

@app.route('/predict')
def predict():
    return 'Sooner will get a model here!'

app.run()
