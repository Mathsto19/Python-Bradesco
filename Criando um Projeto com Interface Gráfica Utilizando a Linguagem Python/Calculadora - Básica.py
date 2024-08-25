while True:
    print("Bem vindo à calculadora")
    num1 = int(input("Digite o primeiro número para realizar a operação: ") )
    num2 = int(input("Digite o segundo número para realizar a operação: ") )
    op = str(input("Digite o símbolo da operação que deseja realizar (+, -, *, /): "))

    if (op == "+"):
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif (op == "-"):
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif (op == "*"):
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif (op == "/"):
        if (num2 != 0):
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Erro: Busque conhecimento")
    else:
        print("Operação Inválida")

    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar != "s" and continuar != "S":
        print("Encerrando a calculadora...")
        break
