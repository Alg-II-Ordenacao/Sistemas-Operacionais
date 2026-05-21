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
                    print("algoritmo da isabele")
                case 2:
                    print("algoritmo do caua")
                case 3:
                    print("algotimo do matheus")
                case 0:
                    return
                case _:
                    print("entrada inválida!")
        except ValueError: print("Digite apenas números inteiros!!")
menu()