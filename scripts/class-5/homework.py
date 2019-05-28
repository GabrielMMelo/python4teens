print("#### Seu dever de casa (matemática) ####")

# Solicite o usuário um problema de matemática
problema = input("Por favor, insira um problema matemático, ou digite 'q' para sair: \n")

# Keep going until the user enters 'q' to quit
while (problema != "q"):

    # Mostre o problema e exiba o resultado usando eval()
    print("A resposta para o problema ", problema, "é:", eval(problema) )

    # Solicite um novo problema
    problema = input("Por favor, insira um novo problema, ou digite 'q' para sair: \n")
