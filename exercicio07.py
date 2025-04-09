soma= 0
for a in range(1,6,1):
    nota = int(input("Digite uma nota: "))
    soma = soma + nota
media = soma/a
print(f"A média é: {media}")