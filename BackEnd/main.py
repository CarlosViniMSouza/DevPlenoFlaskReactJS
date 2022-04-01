from setup_data import somatorio
from flask import Flask
import requests

app = Flask(__name__)

url_api = requests.get(
    'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2000&dataFinal=01/03/2022')

sum = somatorio()

# retorna os dados que pegamos na API


@app.route("/api")
def url_api_bc():
    return url_api.content


@app.route("/valor_total", methods=['GET'])
def valorTotal():
    return f"Valor Total Arrecadado = R${sum}"


if __name__ == '__main__':
    app.run()

# run command in bash: python -m flask run
