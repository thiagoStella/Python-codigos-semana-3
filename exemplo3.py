'''Elabore um programa que solicite um número inteiro ao usuário, em um intervalo entre 1 e 5'''
while True:
    try:
        num = int(input("Digite um número inteiro de 1 a 5: "))
        if 1 <=  num < 5:
            break
        else:
            print("O número deve estar entre 1 e 5!!!")
    except ValueError:
        print("Valor inválido")
print("Número validade foi o :", num)
       