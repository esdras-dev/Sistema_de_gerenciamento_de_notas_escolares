# Lista de alunos (cada aluno é um dicionário)
alunos = [
    {"nome": "Esdras", "disciplina": "Banco de Dados", "nota": 8.5},
    {"nome": "PH", "disciplina": "Estrutura de Dados", "nota": 7.0},
    {"nome": "Gabriel", "disciplina": "Cálculo II", "nota": 9.2},
    {"nome": "Kevin", "disciplina": "POO", "nota": 6.8},
    {"nome": "Victor Hugo", "disciplina": "Calculo I", "nota": 8.8},
]

# Função para mostrar todos os alunos
def mostrar_alunos(lista):
    for aluno in lista:
        print(f"Nome: {aluno['nome']}, Disciplina: {aluno['disciplina']}, Nota: {aluno['nota']}")

# Função para ordenar por nome
def ordenar_por_nome():
    lista_ordenada = sorted(alunos, key=lambda aluno: aluno["nome"])
    print("\nAlunos ordenados por nome:")
    mostrar_alunos(lista_ordenada)

# Função para ordenar por nota
def ordenar_por_nota():
    lista_ordenada = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)
    print("\nAlunos ordenados por nota:")
    mostrar_alunos(lista_ordenada)

# Função para buscar aluno pelo nome
def buscar_por_nome():
    nome = input("Digite o nome do aluno: ")
    encontrado = False
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print(f"\nAluno encontrado: {aluno}")
            encontrado = True
            break
    if not encontrado:
        print("Aluno não encontrado.")

# Menu principal
def menu():
    while True:
        print("\n====== Sistema de Notas Escolares ======")
        print("1. Mostrar todos os alunos: ")
        print("2. Ordenar alunos por nome: ")
        print("3. Ordenar alunos por nota: ")
        print("4. Buscar aluno por nome: ")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_alunos(alunos)
        elif escolha == "2":
            ordenar_por_nome()
        elif escolha == "3":
            ordenar_por_nota()
        elif escolha == "4":
            buscar_por_nome()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu()               
     
 
