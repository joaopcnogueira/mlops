import joblib
from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# loading the model object to predict house prices
model_obj = joblib.load('models/model_prices.pkl')
model = model_obj['model']
features = model_obj['features']


@app.route('/')
def home():
    return 'Hello World'


@app.route('/sentimento/<frase>') # passando a frase na url
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to='en')
    polaridade = tb_en.sentiment.polarity

    return f"""INPUT: {str(tb)};
               INPUT (ENG): {str(tb_en)};
               POLARIDADE: {polaridade}"""


@app.route('/cotacao/', methods=['GET', 'POST'])
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in features]
    preco = model.predict([dados_input])
    return jsonify(preco=preco[0])


app.run(debug=True)
