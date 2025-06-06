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
print("\nMédia das avaliações da compra por loja:")
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
    avaliacoes_ordenadas = dict(sorted(avaliacoes_medias.items(), key=lambda item: item[1], reverse=True))
    sns.barplot(x=list(avaliacoes_ordenadas.keys()), y=list(avaliacoes_ordenadas.values()), palette='viridis')
    plt.title("Média de Avaliações da compra por Loja")
    plt.ylabel("Avaliação Média")
    plt.ylim(0, 5)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# Identificando produtos mais e menos vendidos por loja
print("\nProdutos mais e menos vendidos por loja:")

for loja, df in dados_lojas.items():
    if 'produto' in df.columns:
        vendas_produtos = df['produto'].value_counts()
        
        mais_vendido = vendas_produtos.idxmax()
        menos_vendido = vendas_produtos.idxmin()
        
        print(f"\n🔹 {loja}")
        print(f"Produto mais vendido: {mais_vendido} (Quantidade: {vendas_produtos.max()})")
        print(f"Produto menos vendido: {menos_vendido} (Quantidade: {vendas_produtos.min()})")
        
        # Visualização das vendas por produto
        plt.figure(figsize=(10, 5))
        vendas_produtos.head(10).plot(kind='bar', color='darkgreen')
        plt.title(f'Produtos Mais Vendidos - {loja}')
        plt.xlabel('Produto')
        plt.ylabel('Quantidade Vendida')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

         # Gráfico: Produtos menos vendidos
        plt.figure(figsize=(10, 5))
        vendas_produtos.tail(10).sort_values().plot(kind='bar', color='red')
        plt.title(f'Produtos Menos Vendidos - {loja}')
        plt.xlabel('Produto')
        plt.ylabel('Quantidade Vendida')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()


# Gráfico de comparação do frete médio por loja
fretes_medios = {
    loja: df['frete'].dropna().mean()
    for loja, df in dados_lojas.items() if 'frete' in df.columns
}

if fretes_medios:
    plt.figure(figsize=(8, 4))
    fretes_ordenados = dict(sorted(fretes_medios.items(), key=lambda item: item[1]))
    sns.barplot(x=list(fretes_ordenados.keys()), y=list(fretes_ordenados.values()), palette='Blues')
    plt.title("Custo Médio de Frete por Loja")
    plt.ylabel("Frete Médio (R$)")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# Gráfico de Pizza: Distribuição de categorias da Loja1
if 'categoria_do_produto' in dados_lojas['Loja1'].columns:
    categorias = dados_lojas['Loja1']['categoria_do_produto'].value_counts()
    plt.figure(figsize=(7, 7))
    plt.pie(categorias, labels=categorias.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Categorias - Loja1')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# Gráfico de Linhas: Custo médio de frete por loja
fretes_medios = {
    loja: df['frete'].mean()
    for loja, df in dados_lojas.items() if 'frete' in df.columns
}

plt.figure(figsize=(8, 5))
plt.plot(list(fretes_medios.keys()), list(fretes_medios.values()), marker='o', linestyle='-', color='darkorange')
plt.title('Custo Médio de Frete por Loja')
plt.xlabel('Loja')
plt.ylabel('Frete Médio (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Heatmap: Avaliação Média por Categoria por Loja

# Criar dicionário para armazenar as médias por categoria
avaliacoes_categoria_loja = {}

for loja, df in dados_lojas.items():
    if 'avaliacao_da_compra' in df.columns and 'categoria_do_produto' in df.columns:
        medias = df.groupby('categoria_do_produto')['avaliacao_da_compra'].mean()
        avaliacoes_categoria_loja[loja] = medias

# Combinar tudo em um único DataFrame
df_heatmap = pd.DataFrame(avaliacoes_categoria_loja)

# Preencher valores ausentes com 0 ou outro valor (ex: np.nan)
plt.figure(figsize=(10, 6))
sns.heatmap(df_heatmap, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Heatmap - Avaliação Média por Categoria por Loja')
plt.xlabel('Loja')
plt.ylabel('Categoria do Produto')
plt.tight_layout()
plt.show()
