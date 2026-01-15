# %% vamos construir um programa que realiza um sorteio de um numero entre 1 e 15, o usuario tera 3 tentativas para acertar o numero sorteado a cada tentativa o programa devera informar se o numero digitado e maior ou menor que o numero sorteado, caso acerte de os parabens ao usuario.

import random

def get_input():
    while True:
        try:
            numero_usuario = input("Digite um numero entre 1 e 15: ")
            numero_usuario = int(numero_usuario)
        except ValueError as error:
            print("Entrada invalida. Por favor, digite um numero inteiro entre 1 e 15.")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Numero invalido. Tente novamente. O valor deve ser entre 1 e 15")

        

numero_sorteio = random.randint(1,15)
tentativas = 3


for i in range(tentativas):

    numero_usuario = get_input()

    if numero_sorteio == numero_usuario:
        print("Parabens! Voce acertou o numero.")
        break
    
    elif numero_usuario < numero_sorteio:
        print("O numero digitado e menor que o numero sorteado.")
       
    else:
        print("O numero digitado e maior que o numero sorteado.")
else:
    print(f"Suas tentativas acabaram. O numero sorteado era {numero_sorteio}.")
        

    