horas = int(input("Quantas horas trabalhadas?\n"))
valor = float(input("Qual o valor das horas trabalhadas?\n"))
 
if(horas<=40):
    salario = horas*valor
else:
    salario = valor*40+((valor*1.5)*(horas-40))
 
print(f"Seu salário é: {salario:.2f}")
 