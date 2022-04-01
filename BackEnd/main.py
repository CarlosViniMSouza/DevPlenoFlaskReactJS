from asyncio.windows_events import NULL
from setup_data import somatorio
from flask import Flask, request
import requests

app = Flask(__name__)

url_api = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados'


@app.route("/valor_total", methods=['GET'])
def valorTotal():
    sum = somatorio()
    return f"Valor Total Arrecadado = R${sum}"


@app.route("/api")
# retorna os dados que pegamos na API
def url_api_bc():
    response = requests.get(f"{url_api}").json()
    return f"{response}"


@app.route("/api_solicitacao/<dataInicio>/<dataFim>", methods=['GET', 'POST'])
def apiSolicitacao(dataInicio, dataFim):
    dataInicio = request.args.get('dataInicio', type=dict)
    dataFim = request.args.get('dataFim', type=dict)

    if (dataFim != NULL):
        exit

    response = requests.get(f"{url_api}/{dataInicio}/{dataFim}").json()
    return f"{response}"


if __name__ == '__main__':
    app.run()

# run command in bash: python -m flask run
