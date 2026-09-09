num = int(input("Digite um número: "))
result = ""
if num % 2 == 0:
    result = "par"
else:
    result = "impar"

print(f"O número {num} é {result}")