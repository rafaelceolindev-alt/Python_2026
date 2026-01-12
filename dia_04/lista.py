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
print("Idade máxima",max(idades))
print("Idade mínima",min(idades))
# %%

rafa = ["Rafa", 
        29, 
        True, 
        "Casado", 
        [2500, 3000, 5000, 6000, 8000, 12000],
        ["desenvolvedor","blogueiro"],
        ["Python", "JavaScript", "C++"]]
        


print(rafa[6][0])  # Acessando o primeiro elemento da lista interna
print(rafa[5][1])  # Acessando o segundo elemento da lista interna
print(rafa[4][-1])  # Acessando o último elemento da lista interna
print(rafa[3])  # Acessando o quarto elemento da lista principal
print(rafa[2])  # Acessando o terceiro elemento da lista principal
print(rafa[0])  # Acessando o primeiro elemento da lista principal
print(rafa[-1])  # Acessando o último elemento da lista principal
salarios = rafa[4]
salarios[::2]  # Fatiamento da lista interna
# %%

print(rafa[:2])  # Fatiamento da lista interna
# %%
salarios = rafa[4]
salarios[::3] 
