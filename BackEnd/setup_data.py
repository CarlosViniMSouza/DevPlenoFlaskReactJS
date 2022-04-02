# Bibliotecas:
import pandas as pd
import requests


def dados():
    tabela = requests.get(
        'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json').json()

    dfTabela = pd.DataFrame(tabela)

    soma = [float(string) for string in dfTabela['valor']]

    return (round(sum(soma), 2))
