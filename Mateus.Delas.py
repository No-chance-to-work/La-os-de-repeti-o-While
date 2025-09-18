print("******OPERAÇÔES MATEMÀTICAS******")
print("Escolha uma das opções abaixo. Para encerrar digite sair!!!")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Par ou impar")
print("6 - Primo")
print("7 - Fatorial")
opção = input("Digite a opçao desejada ou <sair> para encerrar")
opçãoMaiuscula =  opção.upper()
while opçãoMaiuscula!="SAIR":
    if opção=="1":
        numero1 = int(input("Digite o primeiro valor: "))
        numero2 = int(input("Digite o segundo valor: "))
        print("O resultado da soma entre",numero1,"e",numero2,"é",numero1 + numero2,".")
    if opção=="2":
        numero1 = int(input("Digite o primeiro valor: "))
        numero2 = int(input("Digite o segundo valor: "))
    print("O resultado da Subtração entre",numero1,"e",numero2,"é",numero1 - numero2,".")
    if opção=="3":
        numero1 = int(input("Digite o primeiro valor: "))
        numero2 = int(input("Digite o segundo valor: "))
    print("O resultado da Multiplicação entre",numero1,"e",numero2,"é",numero1 * numero2,".")
    if opção=="4":
        numero1 = int(input("Digite o primeiro valor: "))
        numero2 = int(input("Digite o segundo valor: "))
    print("O resultado da Divisão entre",numero1,"e",numero2,"é",numero1 / numero2,".")
    if opção=="5":
        numero = int(input("Digite um numero pra saber se ele é impar ou é par:"))
        if numero%2==0:
            print("O numero",numero," é par.")
        else:
            print("O numero ",numero," é impar.")
    if opção=="6":


    if opção=="7":  
            

    input("Pressione ENTER para voltar ao MENU")
    os.system("cls") # pyright: ignore[reportUndefinedVariable]
print("Escolha uma das opções abaixo. Para encerrar digite sair!!!")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Par ou impar")
print("6 - Primo")
print("7 - Fatorial")
