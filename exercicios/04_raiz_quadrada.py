# %% faça um programa que calcule a raiz quadrada de um número fornecido pelo usuário.

numero = (input("Digite um número para calcular a raiz quadrada: "))
numero = int(numero)

raiz_quadrada = numero ** 0.5
print("A raiz quadrada de", numero, "é", raiz_quadrada)
raiz_quadrada = round(raiz_quadrada, 2)
print("Arredondando para duas casas decimais, a raiz quadrada de", numero, "é", raiz_quadrada)