# %% 

def par_impar(numero:int):
    if numero % 2 == 0:
        print("É par")
    else:
        print("É ímpar")

numero = input("Digite um número inteiro: ")
numero = int(numero)

par_impar(numero)