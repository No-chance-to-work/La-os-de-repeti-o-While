soma_positivos = 0
quantidade_negativos = 0
contador = 0
while contador < 2:
    valor = int(input(f"Digite o valor {contador + 1}: "))
    if valor > 0:
        soma_positivos += valor
    if valor < 0:
        quantidade_negativos += 1
    contador += 1
print(f"Soma dos números positivos: {soma_positivos}")
print(f"Quantidade de valores negativos: {quantidade_negativos}")