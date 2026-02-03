while True:
    print('Menu de operações: \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Potência \n 6 - Raiz \n 0 - Encerrar')
    opcao = int(input('Digite qual operação? '))
    if opcao == 0:
        print('Sair da calculadora.')
        break
    if opcao in [1, 2, 3, 4]:
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        if opcao == 1:
            print(n1, '+', n2, '=', n1 + n2)
        elif opcao == 2:
            print(n1, '-', n2, '=', n1 - n2)
        elif opcao == 3:
            print(n1, '.', n2, '=', n1 * n2)
        elif opcao == 4:
            if n2 == 0:
                print('Não pode dividir por zero.')
            if n1 % n2 == 0:
                print(n1, '/', n2, '=', n1 / n2)
            if n1 % n2 != 0:
                print(n1, '/', n2, '=', n1 // n2, 'inteiro e', n1 % n2, 'resto \n OU \n', n1, '/', n2, '=', n1 / n2)
    elif opcao == 5:
        n1 = float(input('Base: '))
        n2 = float(input('Expoente: '))
        if n1 == 0 and n2 == 0:
            print('Confuso.')
        else:
            print(n1, 'elevado a', n2, '=', n1**n2)
    elif opcao == 6:
        n1 = float(input('Radicando: '))
        n2 = float(input('Índice: '))
        if n2 == 0:
            print('Indeterminado.')
        else:
            print('Raíz de grau', n2, 'do número', n1, '=', n1 ** (1/n2))
    else:
        print('Opção inválida.')