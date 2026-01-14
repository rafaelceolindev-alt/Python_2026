# %% algumas funcoes do python

print("Olá, Mundo!")  # Imprime uma mensagem na tela
nome = input("Digite seu nome: ")  # Solicita ao usuário que digite seu nome
print("Olá,", nome)  # Imprime uma saudação personalizada
valor = int(input("Digite um número inteiro: "))  # Solicita um número inteiro e converte para int
print("O número digitado foi:", valor)  # Imprime o número digitado

# %% função simples que retorna o valor incrementado em 1

def f(x):
    return 1 + x

f(10)  # Chama a função f com o argumento 10

print(f(10))  # Imprime o resultado da função f(10)

# %% função com variável intermediária

def f(x):
    resultado = 1 + x
    return resultado

f(20)

