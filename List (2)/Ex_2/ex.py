valorCompra = float(input("Qual foi o valor da compra\n"))
 
if(valorCompra>=200):
    desconto = (valorCompra/10)
    valorDescontado = valorCompra-desconto
    print(f"O valor de R${valorCompra:.2f} da 10% de desconto.\nValor de desconto: {desconto:.2f}\nValor final: {valorDescontado:.2f}")
else:
    print(f"Você não tem desconto, o valor foi de: {valorCompra:.2f}")