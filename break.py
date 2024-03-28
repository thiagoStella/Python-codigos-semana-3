soma = 0
for i in range(5):
    num = int(input("Digite o " + str(i + 1) + " número: "))
    if num == 0:
        break
    soma += num
print("A soma dos numeros é ", soma)