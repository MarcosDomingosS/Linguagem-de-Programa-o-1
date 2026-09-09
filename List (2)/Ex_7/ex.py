nome = input("Digite seu nome: ")
valorCompra = float(input("Digite o valor da compra: "))
valorFrete = 0.00
valorTotal = 0.00

if valorCompra > 150:
    valorFrete = 0
else:
    valorFrete = 20

valorTotal = valorCompra + valorFrete

print(f"• Nome do Cliente: {nome}\n• Valor dos produtos: R${valorCompra:.2f}\n• Valor do frete: R${valorFrete:.2f}\n• Total do pedido: R${valorTotal:.2f}")