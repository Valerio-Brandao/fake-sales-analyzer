# Projeto de Análise de Vendas

Projeto simples feito em Python pra gerar e analisar um conjunto de vendas falsas.
Ele mostra como ler um arquivo CSV e calcular o total vendido por produto.

O projeto faz duas análises:
- Usando apenas Python puro (módulo csv)
- Usando pandas (se estiver instalado)
- E mostra um gráfico com o total de vendas por produto

---

# Como rodar

#1 - Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv

# 2 - ativar ambientes (WINDOWS)
venv\Scripts\activate

#(LINUX/MAC)
source venv/bin/activate


# 3 - instale as dependências
pip install -r requirements.txt

# 4 - Execute o script principal
python analysis.py

