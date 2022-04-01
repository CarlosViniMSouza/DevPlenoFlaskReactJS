from urllib import response
from setup_data import somatorio, dados
from flask import Flask, request
import requests

app = Flask(__name__)

url_api = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados'


class parameters:
    dataInicio = request.args.get('dataInicio')
    dataFim = request.args.get('dataFim')


@app.route("/valor_total", methods=['GET'])
def valorTotal():
    sum = somatorio()
    return f"Valor Total Arrecadado = R${sum}"


@app.route("/api")
# retorna os dados que pegamos na API
def url_api_bc():
    response = requests.get(f"{url_api}").json()
    return f"{response}"


@app.route("/api_solicitacao/<dataInicio>/<dataFim>", methods=['POST'])
def apiSolicitacao():
    pass


"""
    for i in range(0, len(dados.data)):
        if (dados.data[i] == response.keys()):
            return dados.data
        else:
            return 'Not Found'
"""


if __name__ == '__main__':
    app.run()

# run command in bash: python -m flask run
