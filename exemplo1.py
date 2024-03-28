''' Elabore um programa que solicite um número inteiro ao usuário, validando e imprimindo esse número'''
while True:
    try:
        num = int(input("Digite um número: "))
        break
    except ValueError:
        print("Valor inválido")
print("Número que foi validado: ", num) 