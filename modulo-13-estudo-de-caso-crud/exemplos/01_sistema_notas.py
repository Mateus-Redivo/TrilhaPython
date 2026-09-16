alunos = []  # Lista para armazenar os nomes dos alunos
# Lista para armazenar as notas dos alunos (cada elemento é uma lista de notas)
notas = []

# Funçoes auxiliares


def verifica_lista_vazia():
    if not alunos:
        print("Nenhum aluno cadastrado")
        return True
    return False


def receber_aluno():
    try:
        idx = int(input("Digite o número do aluno que deseja alterar: ")) - 1
        if idx < 0 or idx >= len(alunos):
            print("Aluno inválido!")
            return None
        return idx
    except ValueError:
        print("Digite um valor numérico válido!")
        return None


def receber_op_valida():
    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        return -1


def listar_alunos():
    if verifica_lista_vazia():
        return

    print("\nLista de Alunos e Notas:")
    for i in range(len(alunos)):
        aluno = alunos[i]
        if notas[i]:
            total_notas = sum(notas[i])
            quantidade_notas = len(notas[i])
            media = total_notas / quantidade_notas
        else:
            media = 0

        print(f"{i+1}. {aluno} - Notas: {notas[i]} - Média: {media:.2f}")

# Funções do sistema


def menu():
    print("\n" + "=" * 40)
    print("Sistema de Notas")
    print("=" * 40)
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos e Notas")
    print("3. Adicionar Nota")
    print("4. Calcular Média")
    print("5. Alterar Aluno")
    print("6. Excluir Aluno")
    print("7. Popular com Exemplo")
    print("0. Sair")
    print("=" * 40)


def popular_exemplo():
    nomes = ["Mateus", "Isaac", "Henrique", "Henry"]
    notas_exemplo = [[8, 7.5, 9], [6, 7, 8.5], [9, 6.5, 10], [8, 6, 7]]

    for i in range(len(nomes)):
        alunos.append(nomes[i])
        notas.append(notas_exemplo[i])


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ").strip()

    if not nome:
        print("Nome não pode estar vazio!")
        return

    if nome in alunos:
        print(f"Aluno '{nome}' já está cadastrado!")
        return

    alunos.append(nome)
    notas.append([])
    print(f"Aluno '{nome}' cadastrado com sucesso!")


def calcular_media():
    if verifica_lista_vazia():
        return

    print("\nLista de situação dos alunos:")
    for i in range(len(alunos)):
        aluno = alunos[i]
        if notas[i]:
            total_notas = sum(notas[i])
            quantidade_notas = len(notas[i])
            media = total_notas / quantidade_notas
            if media >= 6:
                status = "Aprovado"
            else:
                status = "Reprovado"
        else:
            media = 0
            status = "Sem notas"
        print(f"{i + 1}. Nome: {aluno} - Média: {media:.2f} - Status: {status}")


def adicionar_nota():
    if verifica_lista_vazia():
        return

    listar_alunos()

    try:

        escolha = int(input("\nEscolha o número do aluno: ")) - 1

        if escolha < 0 or escolha >= len(alunos):
            print("Opção inválida!")
            return

        nova_nota = float(
            input(f"Digite uma nova nota para {alunos[escolha]}: "))

        if nova_nota < 0 or nova_nota > 10:
            print("Nota deve estar entre 0 e 10!")
            return

        notas[escolha].append(nova_nota)
        media = sum(notas[escolha]) / len(notas[escolha])
        print(f"Nota {nova_nota} adicionada para '{alunos[escolha]}'!")
        print(f"Notas: {notas[escolha]} - Nova média: {media:.2f}")

    except ValueError:
        print("Por favor, digite um número válido!")


def alterar_aluno():
    if verifica_lista_vazia():
        return

    print("\nAlunos cadastrados:")

    listar_alunos()

    idx = receber_aluno()
    if idx is None:
        return

    novo_nome = input(f"Digite o novo nome para '{alunos[idx]}': ").strip()
    if not novo_nome:
        print("Nome não pode estar vazio!")
        return

    if novo_nome in alunos:
        print(f"Aluno '{novo_nome}' já está cadastrado!")
        return

    nome_antigo = alunos[idx]
    alunos[idx] = novo_nome
    print(f"Aluno '{nome_antigo}' alterado para '{novo_nome}' com sucesso!")


def deletar_aluno():
    if verifica_lista_vazia():
        return

    print("\nAlunos cadastrados:")
    listar_alunos()

    idx = receber_aluno()
    if idx is None:
        return

    nome = alunos[idx]
    confirmacao = input(
        f"Tem certeza que deseja excluir '{nome}'? (s/n): ").strip().lower()
    if confirmacao != 's':
        print("Exclusão cancelada.")
        return

    alunos.pop(idx)
    notas.pop(idx)
    print(f"Aluno '{nome}' excluído com sucesso!")


def main():
    while True:

        menu()

        opcao = receber_op_valida()
        match opcao:
            case 1:
                cadastrar_aluno()
            case 2:
                listar_alunos()
            case 3:
                adicionar_nota()
            case 4:
                calcular_media()
            case 5:
                alterar_aluno()
            case 6:
                deletar_aluno()
            case 7:
                popular_exemplo()
            case 0:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()