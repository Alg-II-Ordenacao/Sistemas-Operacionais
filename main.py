def menu(): #definição do menu com os algoritmos sorteados
    while True:
        print("Qual algoritmo você deseja usar?")
        print("1. Por prioridade, sem preempção ")
        print("2. Por prioridade, com preempção")
        print("3. Round Robin com prioridade e envelhecimento")
        print("0. Sair")

        try:
            escolha = int(input("Digite sua escolha: "))

            match escolha:
                case 1: 
                    matriz = lerMatriz()
                case 2:
                    matriz = lerMatriz()
                case 3:
                    matriz = lerMatriz()
                case 0:
                    return
                case _:
                    print("entrada inválida!")
        except ValueError: print("Digite apenas números inteiros!!")

def lerMatriz(): #leitura das tarefas
    qtdTarefas = int(input("Quantas tarefas terá seu progrma?"))
    matriz = []
    for i in range(qtdTarefas):
        print("Tarefa {i + 1 }: ")
        criacao = int(input("Criação da tarefa: "))
        duracao = int(input("Duração da tarefa: "))
        prioridade = int(input("Prioridade da tarefa: "))
        matriz.append([criacao, duracao, prioridade])   
    return matriz   

menu()
