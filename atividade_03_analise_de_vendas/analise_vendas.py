import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importamos as bibliotecas necessárias para o sistema


# Criamos uma conexão com o banco de dados
# Caso o arquivo não exista, o SQLite cria automaticamente
conn = sqlite3.connect("dados_vendas.db")
cursor = conn.cursor()


# Criamos a tabela responsável por armazenar os dados de vendas
create_table = """
CREATE TABLE IF NOT EXISTS vendas1(
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
"""

cursor.execute(create_table)


# Limpamos os registros anteriores para evitar duplicação
# ao executar novamente o programa
cursor.execute("DELETE FROM vendas1")


# Inserimos os dados de vendas propostos na atividade
cursor.execute("""
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
""")

conn.commit()


# Carregamos os dados do banco em um DataFrame
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conn)

# Convertemos a coluna de data para o formato datetime
# e extraímos o mês de cada venda
df_vendas["data_venda"] = pd.to_datetime(df_vendas["data_venda"])
df_vendas["mes"] = df_vendas["data_venda"].dt.month


# Agrupa as vendas por categoria e apresenta
# o resultado através de um gráfico de barras
def Categoria():

    vendas_categoria = df_vendas.groupby("categoria")["valor_venda"].sum()

    print(
        f"----------------\n"
        f"Total vendido por categoria\n"
        f"{vendas_categoria}"
    )

    sns.barplot(
        x=vendas_categoria.index,
        y=vendas_categoria.values
    )

    plt.title("Valor das vendas por categoria")
    plt.xlabel("Categorias")
    plt.ylabel("Valor vendido R$")
    plt.show()


# Agrupa as vendas por mês e apresenta
# a evolução através de um gráfico de linhas
def Mes():

    vendas_mes = df_vendas.groupby("mes")["valor_venda"].sum()

    print(
        f"---------------\n"
        f"Total vendido por mês\n"
        f"{vendas_mes}"
    )

    sns.lineplot(
        x=vendas_mes.index,
        y=vendas_mes.values
    )

    plt.title("Vendas mensais")
    plt.xlabel("Meses")
    plt.ylabel("Valor vendido R$")
    plt.show()


# Apresenta o resumo geral das vendas e a participação
# de cada categoria no valor total vendido
def Geral():

    total_vendas = df_vendas["valor_venda"].sum()
    ticket_medio = round(df_vendas["valor_venda"].mean(), 2)
    numero_vendas = df_vendas["valor_venda"].count()

    vendas_categoria = df_vendas.groupby("categoria")["valor_venda"].sum()

    print(
        f"Valor total vendido: {total_vendas}\n"
        f"Ticket médio: {ticket_medio}\n"
        f"Número de vendas realizadas: {numero_vendas}"
    )

    plt.pie(
        vendas_categoria.values,
        labels=vendas_categoria.index,
        autopct="%1.1f%%"
    )

    plt.title("Participação de vendas por categoria")
    plt.show()


# Exibe o menu principal do sistema
def Mostrar_menu():

    print("""
===== ANÁLISE DE VENDAS =====
[1] Analisar vendas por categoria
[2] Analisar vendas por mês
[3] Resumo geral das vendas
[0] Sair
""")


# Solicita e valida a opção selecionada pelo usuário
def solicitar_opcao():

    try:
        n = int(input("Escolha uma opção: "))
        return n

    except ValueError:
        print("Selecione um número válido")
        return -1


# Mantém o programa em execução até que o usuário escolha sair
while True:

    Mostrar_menu()

    N = solicitar_opcao()

    if N == -1:
        continue

    elif N == 0:
        print("Programa encerrado.")
        break

    elif N == 1:
        Categoria()

    elif N == 2:
        Mes()

    elif N == 3:
        Geral()

    else:
        print("Opção não cadastrada, tente novamente")
        