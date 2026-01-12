# %% uma maniera de defirmos listas

idades = [28, 42, 35, 27, 19, 33, 41, 29]
print(idades)

# %% listas no python não são arrays

rafa = ["Rafa", 29, 1.75, True]
print(rafa)

type(rafa)

print(rafa[2])  # primeiro elemento
print(rafa[-1])  # último elemento
print(rafa[1:3])  # fatiamento

# %% listas podem conter outras listas

alunos = 
[
["Rafa", 29, 1.75, True],
["Paula", 27, 1.65, False],
["Pedro", 35, 1.80, True],
]

# %%

idades = [28, 42, 35, 27, 19, 33, 41, 29]

print("Soma das idades",sum(idades))
print("Média das idades",sum(idades)/len(idades))
