from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

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

app.run(debug=True)
