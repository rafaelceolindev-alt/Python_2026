# %%

def soma(a, b):
    return a + b

def media(a, b):
    return soma(a, b) / 2

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("A media é:", media(a, b))

# %% uma maneira melhor de organizar o código usando funções

def soma(valores:list) -> float:
    return sum(valores)

def media(valores:list) -> float:
    return soma(valores) / len(valores)

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

print("A média é:", media([a, b, c]))

# %% outra maneira de organizar o código usando funções e tratamento de exceções aqui precisamos lidar com uma quantidade variável de argumentos, desta forma usamos *args alterando apenas a quantidade de argumentos passados para as funções soma e média nao precisando alterar nada mais no código

def soma(a, b, *args):
    valores = [a, b] + list(args)
    return sum(valores)

def media(a, b, *args):
    return soma(a, b, *args) / (2 + len(args))

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número (ou deixe em branco para pular): ") or 0)
d = float(input("Digite o quarto número (ou deixe em branco para pular): ") or 0)

print("A média é:", media(a, b, c, d))