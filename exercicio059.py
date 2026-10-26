print("Criando opções em um Menu")

sair_programa = False
while not sair_programa:
    tem_numero = True

    primeiro_valor = int(input("Primeiro valor: "))
    segundo_valor = int(input("Segundo valor: "))

    while tem_numero:
        print("--------------------------")

        print("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do Programa")
        opcao = int(input("Qual sua opção: "))

        if opcao == 1:
            soma = primeiro_valor + segundo_valor
            print(f"O resultado de {primeiro_valor} + {segundo_valor} é {soma}")
        elif opcao == 2:
            produto = primeiro_valor * segundo_valor
            print(f"O resultado de {primeiro_valor} x {segundo_valor} é {produto}")
        elif opcao == 3:
            if primeiro_valor > segundo_valor:
                print(f"O valor {primeiro_valor} é maior que {segundo_valor}.")
            elif segundo_valor > primeiro_valor:
                print(f"O valor {segundo_valor} é maior que {primeiro_valor}.")
            elif primeiro_valor == segundo_valor:
                print(f"Os valores ({primeiro_valor}) são iguais!")
        elif opcao == 4:
            tem_numero = False
        elif opcao == 5:
            print("Fim do programa!")
            sair_programa = True
            tem_numero = False
        else:
            print("Opção Inválida! Tente novamente.")


