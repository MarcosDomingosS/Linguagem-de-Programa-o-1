n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
 
if(n2==0):
    resultado = n1/n2
    print(f"A divisão do primeiro pelo segundo é: {resultado}")
else:
    print("Não é possível realizar a divisão por zero")