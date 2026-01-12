# %% quais numeros de 1 a 100 são divisíveis por 4

count = 4
while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count, "é divisível por 4")
    count = count + 1

