soma = 0
for i in range(4):
    soma += int(input("Digite a nota " + str(i+1) + ": "))

print("Média: " + str(soma/4))