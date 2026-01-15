# %% exemplo com raiz quadrada, dessa forma abaixo, mas sera que o python ja nao tem uma funcao pronta para isso? podemos importar do modulo math

def sqrt(numero):
    return numero ** (1/2)

sqrt(9)

# %% importando o modulo math e usando a funcao sqrt dele

import math

math.sqrt(9)
math.pi
math.factorial(5)

# %% criando um modulo personalizado  do pi e importando ele

from math import pi

pi

# %% importando um modulo e nomeando ele com um apelido (alias) 

import math as mh

mh.sqrt(16)

# %% importando funcoes especificas de um modulo

from math import sqrt, factorial

sqrt(25)
factorial(6)