import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import unicodedata

def limpar_colunas(df):
    colunas_limpa = []
    for col in df.columns:
        # Remover acentos
        col = unicodedata.normalize('NFKD', col).encode('ASCII', 'ignore').decode('utf-8')
        # Tirar espaços extras e colocar em minúsculas
        col = col.strip().lower()
        # Substituir espaços por underline
        col = col.replace(' ', '_')
        colunas_limpa.append(col)
    df.columns = colunas_limpa
    return df

# Dicionário com URLs de cada loja
urls = {
    'Loja1': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
    'Loja2': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
    'Loja3': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
    'Loja4': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"
}

# Carregando os dados com colunas limpas
dados_lojas = {nome: limpar_colunas(pd.read_csv(url)) for nome, url in urls.items()}

# Faturamento por loja
faturamentos = {loja: df['preco'].sum() for loja, df in dados_lojas.items()}

print("\nFaturamento por loja:")
for loja, valor in faturamentos.items():
    print(f"{loja}: R$ {valor:,.2f}")

# Gráfico de faturamento
plt.figure(figsize=(8, 5))
plt.bar(faturamentos.keys(), faturamentos.values(), color='teal')
plt.title('Faturamento Total por Loja')
plt.xlabel('Loja')
plt.ylabel('Faturamento (R$)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Vendas por categoria
for loja, df in dados_lojas.items():
    if 'categoria_do_produto' in df.columns:
        categoria_counts = df['categoria_do_produto'].value_counts()
        plt.figure(figsize=(8, 5))
        categoria_counts.plot(kind='bar', color='slateblue')
        plt.title(f'Vendas por Categoria - {loja}')
        plt.xlabel('Categoria')
        plt.ylabel('Quantidade de Vendas')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print(f"A loja {loja} não possui a coluna 'categoria_do_produto'")

# Média das avaliações
print("\nMédia das avaliações por loja:")
avaliacoes_medias = {}
for loja, df in dados_lojas.items():
    if 'avaliacao_da_compra' in df.columns:
        media = df['avaliacao_da_compra'].mean()
        avaliacoes_medias[loja] = media
        print(f"{loja}: {media:.2f}")
    else:
        print(f"A loja {loja} não possui a coluna 'avaliacao_da_compra'")

# Gráfico de médias de avaliação
if avaliacoes_medias:
    plt.figure(figsize=(8, 4))
    sns.barplot(x=list(avaliacoes_medias.keys()), y=list(avaliacoes_medias.values()), palette='viridis')
    plt.title("Média de Avaliações por Loja")
    plt.ylabel("Avaliação Média")
    plt.ylim(0, 5)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()