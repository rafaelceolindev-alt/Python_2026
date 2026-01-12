# %%

idades = []

while True:
    idade = input("Digite uma idade:" )

    if idade == "":
        break
    idades.append(int(idade))
print(idades)

media = sum(idades) / len(idades) 
minimo = min(idades) 
maximo = max(idades) 
quantidade = len(idades) 
print(f"Média: {media}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print(f"Quantidade: {quantidade}")

print("idades")
print("minimo")
print("maximo")
print("quantidade")