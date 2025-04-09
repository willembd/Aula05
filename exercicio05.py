cont= 0
for a in range(1,5,1):
    n = int(input("Digite um Valor: "))
    if n < 0:
        cont+=1

print(f"{cont} Número Negativos foram digitados")