nomeVendedor = input("Digite o nome do vendedor: ")
totalMes = float(input("Digite o total vendido no mês: "))
metaMensal = 10000

if totalMes < metaMensal:
    print(f"Falta {(metaMensal - totalMes):.2f} para {nomeVendedor} atingir a meta")
else:
    print(f"{nomeVendedor} atingiu a meta")
