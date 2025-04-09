cont1=0
cont2=0

for a in range(1,5,1):
    n = int(input("Digite um valor: "))
    if n>=10 and n<=20:
        cont1+=1
    else:
        cont2+=1
print(f"{cont1} valores estão dentro do intervalo de 10 á 20")
print(f"{cont2} valores estão fora do intervalo de 10 á 20")