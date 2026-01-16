# %%

a = 5
b = 1

print(a)
print(b)

# %%

c = a
a = b
b = c
print(a)
print(b)

# %% isso é um unpack, descompactar a lista ou a tupla em um ou mais elementos

a, b = b, a
print(a)
print(b)
# %%

b, a = a, b

# %% pegando os dois primeiros 

a, b, *resto = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a, b, resto)
# %% pegando o primeiro e o ultimo

a,*resto, b  = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a, b, resto)

# %% pegando os ultimos

*resto, a, b  = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a, b, resto)

# %% o args é a mesma coisa das situações acima

def soma(a, *args):
    total = a + sum(args)
    return  total

soma(1,2,4,7,10)

# %%

def soma_quatro(a,b,c,d):
    return a+b+c+d

values = [1,2,3,4]
soma_quatro(*values)