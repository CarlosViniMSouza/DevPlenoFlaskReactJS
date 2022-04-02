"""
# This file is a test model for main.py!!

from flask import Flask
import pandas as pd
import requests

app = Flask(__name__)

dataIni = "01/01/2000"
dataFim = "01/01/2002"

URL_Table = requests.get(
    f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial={dataIni}&dataFinal={dataFim}").content

URL = requests.get(
    f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial={dataIni}&dataFinal={dataFim}").json()


@app.route("/")
def welcome():
    return "<h2>Hello!</h2>"


@app.route("/requisicao", methods=['GET'])
def requisicao():
    return URL_Table


@app.route("/valor_resp_interv")
def valor_resp():
    table = pd.DataFrame(URL)
    soma = [float(string) for string in table['valor']]
    return f"<p>A soma dos valores entre {dataIni} e {dataFim} eh = R${round(sum(soma), 2)}</p>"


if __name__ == '__app__':
    app.run(debug=True)
"""
