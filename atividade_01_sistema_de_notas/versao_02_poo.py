# Dicionário utilizado para armazenar os alunos cadastrados,
# utilizando a matrícula como chave
Cadastro = {}


# Classe responsável por representar cada aluno cadastrado
class alunos:

    def __init__(self, nome, nota_geo, nota_mat, nota_port,
                 nota_ing, nota_fis, matricula):

        self.nome = nome
        self.nota_geo = nota_geo
        self.nota_mat = nota_mat
        self.nota_port = nota_port
        self.nota_ing = nota_ing
        self.nota_fis = nota_fis
        self.matricula = matricula


    # Exibe os dados, notas, média e situação do aluno
    def Consultar_status(self):

        print(
            f"--- {self.matricula} ---\n"
            f"Nome: {self.nome}\n"
            f"Nota Geografia: {self.nota_geo}\n"
            f"Nota Matemática: {self.nota_mat}\n"
            f"Nota Português: {self.nota_port}\n"
            f"Nota Inglês: {self.nota_ing}\n"
            f"Nota Física: {self.nota_fis}"
        )

        N = self.Consultar_media()

        if N >= 7:
            print(f"Situação atual: Aprovado\nMédia: {N}")
        else:
            print(f"Situação atual: Reprovado\nMédia: {N}")


    # Calcula e retorna a média das notas do aluno
    def Consultar_media(self):

        valores = [
            self.nota_fis,
            self.nota_geo,
            self.nota_ing,
            self.nota_mat,
            self.nota_port
        ]

        return round(sum(valores) / len(valores), 2)


    # Salva o objeto do aluno no dicionário utilizando a matrícula
    # e exibe sua situação atual
    def Salvar_e_verificar(self):

        print("Dados registrados")

        Cadastro[self.matricula] = self

        N = self.Consultar_media()

        if N >= 7:
            print(f"Situação atual: Aprovado\nMédia: {N}")
        else:
            print(f"Situação atual: Reprovado\nMédia: {N}")


# Coleta os dados necessários para realizar o cadastro do aluno
def Coletar():

    t1 = True

    while t1:
        try:
            d1 = int(input("Digite a matrícula: "))
            t1 = False

        except ValueError:
            print("Insira apenas números")
            continue


    t2 = True

    while t2:
        try:
            d2 = float(input("Digite a nota de Geografia (0 a 10): "))

            if d2 < 0 or d2 > 10:
                print("A nota deve estar entre 0 e 10")
                continue

            t2 = False

        except ValueError:
            print("Insira apenas números")
            continue


    t3 = True

    while t3:
        try:
            d3 = float(input("Digite a nota de Matemática (0 a 10): "))

            if d3 < 0 or d3 > 10:
                print("A nota deve estar entre 0 e 10")
                continue

            t3 = False

        except ValueError:
            print("Insira apenas números")
            continue


    t4 = True

    while t4:
        try:
            d4 = float(input("Digite a nota de Português (0 a 10): "))

            if d4 < 0 or d4 > 10:
                print("A nota deve estar entre 0 e 10")
                continue

            t4 = False

        except ValueError:
            print("Insira apenas números")
            continue


    t5 = True

    while t5:
        try:
            d5 = float(input("Digite a nota de Inglês (0 a 10): "))

            if d5 < 0 or d5 > 10:
                print("A nota deve estar entre 0 e 10")
                continue

            t5 = False

        except ValueError:
            print("Insira apenas números")
            continue


    t6 = True

    while t6:
        try:
            d6 = float(input("Digite a nota de Física (0 a 10): "))

            if d6 < 0 or d6 > 10:
                print("A nota deve estar entre 0 e 10")
                continue

            t6 = False

        except ValueError:
            print("Insira apenas números")
            continue


    nome = input("Digite o nome do aluno: ")

    # Cria um novo objeto da classe alunos com os dados informados
    novo_aluno = alunos(nome, d2, d3, d4, d5, d6, d1)

    novo_aluno.Salvar_e_verificar()


# Exibe o menu principal do sistema
def mostrar_menu():

    print("""
------ SISTEMA ------
[1] Cadastrar aluno
[2] Verificar situação
[3] Sair
---------------------
""")


# Solicita e valida a opção selecionada no menu
def Solicitar_opcao():

    try:
        return int(input("Escolha uma opção: "))

    except ValueError:
        return 0


# Consulta um aluno utilizando sua matrícula
def verificar():

    t1 = True

    while t1:

        try:
            mat = int(input("Digite a matrícula: "))

            if mat in Cadastro:
                Cadastro[mat].Consultar_status()
                t1 = False

            else:
                print("Matrícula não cadastrada na base de dados. Tente novamente.")

            continue

        except ValueError:
            print("Digite apenas números")
            continue


# Mantém o sistema em execução até que o usuário escolha sair
while True:

    mostrar_menu()

    op = Solicitar_opcao()

    if op == 1:
        Coletar()

    elif op == 2:
        verificar()

    elif op == 3:
        print("Programa encerrado.")
        break

    else:
        print("Selecione uma opção válida")