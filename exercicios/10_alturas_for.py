# %% calcular a altura média de 5 pessoas usando for    


soma_alturas = 0
count = 5

for i in range(count):
    altura = input("Digite a altura da pessoa em metros (ex: 1.75): ")
    altura = float(altura)
    soma_alturas += altura
altura_media = soma_alturas / 5
print("A altura média das 5 pessoas é: {:.2f} metros".format(altura_media))