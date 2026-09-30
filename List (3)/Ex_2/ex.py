maior = 0
contador = 0

while contador < 10:
    num = float(input("Digite um número: "))
    if contador == 0:
        maior = num
    else:
        if num > maior:
            maior = num
    contador += 1

print(f"O maior número é: {maior}")