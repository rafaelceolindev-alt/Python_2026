# %%
# calcular o saldo total de uma conta bancária
saldo_total = 0
while True:
    saldo = input("Digite o valor do saldo (ou 'sair' para encerrar): ")
    if saldo == 'sair':
        break
    saldo_total += float(saldo)
print(saldo_total)

    