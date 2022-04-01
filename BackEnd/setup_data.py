# Bibliotecas:
import pandas as pd

# Inserindo dados:
table = pd.read_csv("data/table2_ipca2_tratado.csv")

# Precisamos criar um index 'id'na tabela.
# id = list(range(len(table)))
# table['id'] = id  # id add na table


def somatorio():
    # Somando valores:
    tab = table['valor']
    total = tab.sum()
    return total


"""
# vamos pensar em como puxar 12 linhas a cada requisicao:

data = input("digite o dia desejado (ex.: 01/01/2000) = ")

for i in range(0, len(table)):
    if (data == table['data'][i]):
        for j in range(table['id'][i], table['id'][i + 11]):
            print(table['data'][j])
            break
    else:
        pass
"""
