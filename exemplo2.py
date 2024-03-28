''' Elabore um programa que solicite um número decimal ao usuário, validando e imprimindo esse número'''
while True:
    try:
        num = float(input("Digite um número decimal: "))
        break
    except ValueError:
        print("Valor inválido")
print("Número validado foi: ", num)