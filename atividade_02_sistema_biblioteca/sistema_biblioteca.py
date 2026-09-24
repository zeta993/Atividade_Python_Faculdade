# Lista utilizada para armazenar os livros cadastrados
Livros = []


# Classe responsável por representar cada livro
class Livro:

    def __init__(self, Titulo, Autor, Genero, Quantidade):
        self.Titulo = Titulo
        self.Autor = Autor
        self.Genero = Genero
        self.Quantidade = Quantidade


    # Exibe as informações do livro
    def Consultar(self):

        print(
            f"Título: {self.Titulo}\n"
            f"Autor: {self.Autor}\n"
            f"Gênero: {self.Genero}\n"
            f"Quantidade disponível: {self.Quantidade}"
        )


# Coleta os dados e cadastra um novo livro
def Cadastrar():

    while True:

        Titulo = input("Qual o título do livro? ")
        Autor = input("Quem é o autor? ")

        # Verifica se o mesmo livro e autor já estão cadastrados
        livro_existente = False

        for livro in Livros:

            if livro.Titulo == Titulo and livro.Autor == Autor:
                livro_existente = True
                break

        if livro_existente:
            print("Este livro já está cadastrado")
            continue

        Genero = input("Qual o gênero? ")

        try:
            Quantidade = int(input("Quantas cópias? "))

            if Quantidade < 0:
                print("Digite um número válido")
                continue

            # Cria um novo objeto da classe Livro
            Novo_Livro = Livro(
                Titulo,
                Autor,
                Genero,
                Quantidade
            )

            # Armazena o objeto criado na lista
            Livros.append(Novo_Livro)

            print("Livro cadastrado com sucesso")
            break

        except ValueError:
            print("Digite apenas números")


# Exibe o menu principal da biblioteca
def mostrar_menu():

    print("""
------ BIBLIOTECA ------
[1] Cadastrar Livro
[2] Consultar Livro
[3] Sair
------------------------
""")


# Solicita e valida a opção selecionada no menu
def Solicitar_opcao():

    try:
        return int(input("Escolha uma opção: "))

    except ValueError:
        return 0


# Procura um livro cadastrado através do título
def Validar():

    titulo = input("Digite o título do livro: ")

    for livro in Livros:

        if livro.Titulo == titulo:
            livro.Consultar()
            return

    print("Livro não cadastrado")


# Mantém o sistema em execução até que o usuário escolha sair
while True:

    mostrar_menu()

    n = Solicitar_opcao()

    if n == 1:
        Cadastrar()

    elif n == 2:
        Validar()

    elif n == 3:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida")