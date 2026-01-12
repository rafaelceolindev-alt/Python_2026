# %% Faça um programa que vende uma garrafa de água natural por R$ 5,00.
# se for com gás, o preço sobe para R$ 7,00.
# Pergunte ao usuário se ele quer com ou sem gás e mostre o preço final.     

texto = """Bem-vindo à venda de garrafas de água!
Escolha o tipo de água que deseja comprar:
1. Água sem gás - R$ 5,00
2. Água com gás - R$ 7,00
Digite '1' para sem gás ou '2' para com gás."""

opcao = input(texto)

preco = 0
if opcao == '1':
    preco = 5.00
    print("Você escolheu água sem gás. O preço  é R$ {:.2f}".format(preco))
elif opcao == '2':
    preco = 7.00
    print("Você escolheu água com gás. O preço é R$ {:.2f}".format(preco)) 
if preco == 0:
    print("Opção inválida. Por favor, escolha '1' para sem gás ou '2' para com gás.")

else:
    quantidade = input("Quantas garrafas você deseja comprar? ")
    quantidade = int(quantidade)
    total = preco * quantidade
    print("O total a pagar é R$ {:.2f}".format(total))

