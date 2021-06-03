import joblib

from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob

# creating the app API
app = Flask(__name__)

# handle API authorization
app.config['BASIC_AUTH_USERNAME'] = 'joao'
app.config['BASIC_AUTH_PASSWORD'] = '123456'
basic_auth = BasicAuth(app)

# loading the model object to predict house prices
model_obj = joblib.load('models/model_prices.pkl')
model = model_obj['model']
features = model_obj['features']


# endpoint inicial
@app.route('/')
def home():
    return 'Hello World'


# endpoint para previsão de sentimentos
@app.route('/sentimento/<frase>') # passando a frase na url
@basic_auth.required
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to='en')
    polaridade = tb_en.sentiment.polarity

    return f"""INPUT: {str(tb)};
               INPUT (ENG): {str(tb_en)};
               POLARIDADE: {polaridade}"""


# endpoint para previsão de preço de casas
@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in features]
    preco = model.predict([dados_input])
    return jsonify(preco=preco[0])


app.run(debug=True)
