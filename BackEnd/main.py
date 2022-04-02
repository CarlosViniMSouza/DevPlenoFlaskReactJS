# Full Example to Docs
from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from HelloApiHandler import HelloApiHandler
from setup_data import dados
import pandas as pd
import requests


app = Flask(__name__, static_url_path='',
            static_folder='../BackEnd/templates')
CORS(app)

api = Api(app)
info = dados()

dataIni = "01/01/2000"
dataFim = "01/01/2002"

URL_Table = requests.get(
    f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial={dataIni}&dataFinal={dataFim}").content

URL = requests.get(
    f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial={dataIni}&dataFinal={dataFim}").json()


@app.route("/")
def servidor():
    return send_from_directory(app.static_folder, 'setup.html')


@app.route("/somatorio")
def somatorio():
    return f"<p>A soma de todos os valores eh = ${info}</p>"


@app.route("/requisicao", methods=['GET'])
def requisicao():
    return URL_Table


@app.route("/valor_resp_interv")
def valor_resp():
    table = pd.DataFrame(URL)
    soma = [float(string) for string in table['valor']]
    return f"<p>A soma dos valores entre {dataIni} e {dataFim} eh = R${round(sum(soma), 2)}</p>"


api.add_resource(HelloApiHandler, '/flask/hello')


if __name__ == '__main__':
    app.run(debug=True)
