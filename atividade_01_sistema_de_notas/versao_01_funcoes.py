# Lista utilizada para armazenar as notas cadastradas
Notas = []


# Coleta e valida as notas informadas pelo usuário
def Coletar_Notas():
    try:
        N = int(input("Quantas notas deseja cadastrar: "))

        if N <= 0:
            print("Opção inválida")
            return

    except ValueError:
        print("Digite apenas números")
        return

    # Repete o cadastro de acordo com a quantidade informada
    for i in range(N):

        while True:
            try:
                D = float(input("Digite a nota: "))

                # Verifica se a nota está dentro do intervalo permitido
                if D < 0 or D > 10:
                    print("Nota inválida")
                    continue

                Notas.append(D)
                break

            except ValueError:
                print("Digite apenas números")

    return N


# Exibe as notas cadastradas e calcula a média
def Calcular_media():

    if len(Notas) > 0:

        for i in Notas:
            print(f"Nota: {i}")

        media = sum(Notas) / len(Notas)

        return media

    else:
        # Retorna -1 caso ainda não existam notas cadastradas
        return -1


# Verifica a situação do aluno a partir da média calculada
def exibir_resultado(Nome, Media):

    # Arredonda a média para duas casas decimais
    Media = round(Media, 2)

    if Media >= 7:
        print(f"O aluno {Nome} está aprovado, com média: {Media}")

    else:
        print(f"O aluno {Nome} está reprovado, com média: {Media}")


# Exibe o menu principal do sistema
def Mostrar_menu():

    print("""
------ SISTEMA ------
[1] Cadastrar Notas
[2] Verificar aprovação
[3] Sair
---------------------
""")


# Solicita e valida a opção selecionada no menu
def Solicitar_opcao():

    try:
        return int(input("Escolha uma opção: "))

    except ValueError:
        return 0


# Mantém o programa em execução até que o usuário escolha sair
while True:

    Mostrar_menu()

    N = Solicitar_opcao()

    if N == 1:
        Coletar_Notas()

    elif N == 2:

        Nome = input("Digite o nome do aluno: ")

        Media = Calcular_media()

        if Media >= 0:
            exibir_resultado(Nome, Media)

        else:
            print("Ainda não há notas cadastradas")

    elif N == 3:
        print("Programa encerrado.")
        break

    else:
        print("Selecione uma opção válida")