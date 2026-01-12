# %% faça um programa que leia a altura de 5 pessoas e ao final mostre a altura média digitada

soma_alturas = 0
count = 5

while count > 0:
    altura = input("Digite a altura da pessoa em metros (ex: 1.75): ")
    altura = float(altura)
    soma_alturas += altura
    count -= 1
altura_media = soma_alturas / 5
print("A altura média das 5 pessoas é: {:.2f} metros".format(altura_media))