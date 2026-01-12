# %%

#escreva um programa que receba uma lista de numeros do usuario e conte quantas vezes um numero especifico aparece na lista, solicite o numero ao usuario

lista = [1, 2, 3, 4, 5, 1, 2, 1, 3, 1, 6, 1, 7, 8, 1, 9, 1, 10, 1, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15]


numero = (input("Digite o número que deseja contar na lista: "))
numero = int(numero)

contador = 0
for i in lista:
    if i == numero:
        contador += 1

print(f"O número {numero} aparece {contador} vezes na lista.")
# %%
