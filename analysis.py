# analysis.py
# Projeto simples de análise de vendas (teste técnico BigData)
# Feito por um estagiário júnior
# Gera dados falsos de vendas, analisa e mostra um gráfico

import csv
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt  # biblioteca pra gerar gráfico

# tenta importar o pandas, mas o código ainda roda sem ele
try:
    import pandas as pd
except ImportError:
    pd = None


def gerar_vendas_fake(caminho='sales.csv', quantidade=200):
    """
    Cria um arquivo CSV com dados falsos de vendas.
    Cada linha tem: id, data, produto, quantidade e preço.
    """
    produtos = ['Caneta', 'Caderno', 'Mochila', 'Borracha', 'Calculadora']
    data_inicial = datetime(2024, 1, 1)
    linhas = []

    # gera várias vendas aleatórias
    for i in range(quantidade):
        produto = random.choice(produtos)
        data = data_inicial + timedelta(days=random.randint(0, 365))
        qtd = random.randint(1, 5)
        preco = round(random.uniform(5, 200), 2)
        linhas.append([i + 1, data.strftime('%Y-%m-%d'), produto, qtd, preco])

    # salva o arquivo CSV
    with open(caminho, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(['id', 'data', 'produto', 'quantidade', 'preco'])
        escritor.writerows(linhas)

    print(f'✅ Arquivo {caminho} criado com {quantidade} registros!')


def analisar_python_puro(caminho='sales.csv'):
    """
    Lê o CSV e soma o total vendido por produto.
    Feito sem usar bibliotecas externas.
    """
    totais = {}

    # abre o arquivo CSV e percorre as linhas
    with open(caminho, newline='', encoding='utf-8') as f:
        leitor = csv.DictReader(f)

        for linha in leitor:
            produto = linha['produto']
            qtd = int(linha['quantidade'])
            preco = float(linha['preco'])

            
            if produto not in totais:
                totais[produto] = 0

            
            totais[produto] += qtd * preco

    print('\n💰 Total de vendas por produto (Python puro):')
    for produto, total in totais.items():
        print(f' - {produto}: R$ {total:.2f}')

    return totais


def analisar_com_pandas(caminho='sales.csv'):
    """
    Faz a mesma análise usando pandas (se estiver instalado).
    """
    if pd is None:
        print('⚠️ Pandas não instalado. Rode "pip install pandas" para usar essa função.')
        return None

    df = pd.read_csv(caminho, parse_dates=['data'])
    df['faturamento'] = df['quantidade'] * df['preco']
    resumo = df.groupby('produto')['faturamento'].sum().reset_index()

    print('\n📊 Total de vendas por produto (pandas):')
    print(resumo.to_string(index=False))

    return resumo


def gerar_grafico(totais):
    """
    Gera um gráfico de barras com o total de vendas por produto.
    """
    produtos = list(totais.keys())
    valores = list(totais.values())

    plt.figure(figsize=(8, 5))
    plt.bar(produtos, valores, color='royalblue')
    plt.title('Total de Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Valor Total (R$)')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


def main():
    """
    Executa todo o processo:
    1. Gera o CSV
    2. Analisa com Python puro
    3. Analisa com pandas
    4. Mostra o gráfico
    """
    gerar_vendas_fake()
    totais = analisar_python_puro()
    analisar_com_pandas()
    gerar_grafico(totais)


if __name__ == '__main__':
    main()
