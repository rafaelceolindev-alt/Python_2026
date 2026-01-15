# %% tabuada.py

numero = 2

print("Tabuada do", numero)
print("2 x 1 =", numero * 1)
print("2 x 2 =", numero * 2)
print("2 x 3 =", numero * 3)
print("2 x 4 =", numero * 4)
print("2 x 5 =", numero * 5)
print("2 x 6 =", numero * 6)
print("2 x 7 =", numero * 7)
print("2 x 8 =", numero * 8)
print("2 x 9 =", numero * 9)
print("2 x 10 =", numero * 10)
print("---------------------")    
# %% uma forma melhorada usando loop for

while True:
    entrada = input("Digite um número para ver a tabuada (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        print("Encerrando o programa. Até mais!")
        break
    if not entrada.isdigit():
        print("Por favor, digite um número válido.")
        continue
    numero = int(entrada)
    print("Tabuada do", numero)
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print("---------------------")
    # %% usando while
numero = 2
count = 1
    

while count <= 100:
    print(numero, "x", count, "=", numero * count)
    count = count + 1
print("---------------------")

# %%
