num = -1
result = 1

while num < 0:
    num = int(input("Digite um número inteiro positivo ou igual a zero: "))

for n in range (num):
    result *= (n+1)

print(f"{num}! = {result}")