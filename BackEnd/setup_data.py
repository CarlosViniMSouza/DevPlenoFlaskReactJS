# Bibliotecas:
import pandas as pd

# Inserindo dados:
table = pd.read_csv("data/table2_ipca2_tratado.csv")


class dados:
    data = table['data']
    valor = table['valor']


def somatorio():
    # Somando valores:
    tab = table['valor']
    total = tab.sum()
    return total
