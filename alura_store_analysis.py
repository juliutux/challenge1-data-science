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


# Gráfico de barras do faturamento
plt.figure(figsize=(8, 5))
plt.bar(faturamentos.keys(), faturamentos.values(), color='teal')
plt.title('Faturamento Total por Loja')
plt.xlabel('Loja')
plt.ylabel('Faturamento (R$)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# Quantidade de produtos vendidos por categoria em cada loja
for loja, df in dados_lojas.items():
    categoria_counts = df['Categoria do Produto'].value_counts()
    plt.figure(figsize=(8, 5))
    categoria_counts.plot(kind='bar', color='slateblue')
    plt.title(f'Vendas por Categoria - {loja}')
    plt.xlabel('Categoria')
    plt.ylabel('Quantidade de Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()