import pandas as pd
import matplotlib.pyplot as plt

# Dicionário com URLs de cada loja
urls = {
    'Loja1': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
    'Loja2': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
    'Loja3': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
    'Loja4': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"
}

# Carregando os dados diretamente das URLs
dados_lojas = {nome: pd.read_csv(url) for nome, url in urls.items()}

# Visualizar os primeiros dados da Loja1
#print(dados_lojas['Loja2'].head())

# Análise de faturamento total por loja
faturamentos = {loja: df['Preço'].sum() for loja, df in dados_lojas.items()}

print("\nFaturamento por loja:")
for loja, valor in faturamentos.items():
    print(f"{loja}: R$ {valor:,.2f}")
