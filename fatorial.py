fatorial = 1
expressao = "Expressaão: "
num = int(input("Digite um número para o cálculo fatorial: "))
for i in range(num, 0, -1):
    fatorial *= i
    expressao += str(i)
    if i > 1:
        expressao += " * "
print("O valor do fatorial é de", num, "é", fatorial, expressao)