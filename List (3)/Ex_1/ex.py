pos = 0
neg =0
zero = 0
 
for num in range(11):
    numero = int(input(f"Diga o {num}° número\n"))
    if(numero==0):
        zero += 1
    elif(numero>0):
        pos += 1
    elif(numero<0):
        neg += 1
 
print(f"Foram {pos} positivos, {neg} negativos, e {zero} zeros")