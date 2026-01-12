
# %% iterando sobre cada letra do nome

nome = "Rafael Ceolin"

for letra in nome:
    print(letra)

# %% somando números de 1 a 10
soma = 0
for numero in range(1, 11):
    soma += numero
print("A soma dos números de 1 a 10 é:", soma)
# %% brincando com tabuada e for

numero = 2
max_numero = 100

for i in range(1, max_numero + 1):
    print(numero, "x", i, "=", numero * i)

# %%
# quais numeros de 1 a 100 são divisíveis por 4 - versão 2

for i in range(4, 101):
    if i % 4 == 0:
        print(i, "é divisível por 4")