num = 0
isPrimo = True

while num <= 0:
    num = int(input("Digite um número inteiro positivo: "))

for n in range(2, num):
    if num%n == 0:
        isPrimo = False
        break

if num == 1: isPrimo = False

if isPrimo:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")
