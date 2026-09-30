num = 0
isPrimo = False

while num <= 0:
    num = int(input("Digite um número inteiro positivo: "))

for n in range(1, num):
    if n == 1: 
        continue
    if num%n != 0:
        isPrimo = True
    print (n)


if isPrimo:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")
