numero = int(input("Digite um número para descobrir seus divisores\n"))
 
for n in range(1,numero+1):
    if(numero%n==0):
        print(f"{n}")