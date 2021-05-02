import requests

url = "http://127.0.0.1:5000/cotacao/"

dados = {
    "tamanho": 120,
    "ano": 2001,
    "garagem": 2
}

auth = requests.auth.HTTPBasicAuth('joao', '123456')
response = requests.post(url, json=dados, auth=auth)
print(response.text)