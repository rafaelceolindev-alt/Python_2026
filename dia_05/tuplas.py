# %% listas sao mutaveis podem ser usadas para representar dados que podem ser alterados

dados_rafa = ["Rafa", 29, "Desenvolvedor", ["São Paulo", "curitiba"]]
dados_rafa

# %% adicionando um novo dado na lista

dados_rafa.append("3232323")
dados_rafa

# %% tuplas sao listas imutaveis podem ser usadas para representar dados que nao devem ser alterados pode ser com () ou sem nada

tupla_rafa = ("Rafa", 29, "Desenvolvedor", ["São Paulo", "curitiba"])

print(type(tupla_rafa))
print(tupla_rafa)

# %% tentando adicionar um novo dado na tupla
tupla_rafa.append("3232323")  # AttributeError: nao podemos incluir novos dados em uma tupla

# %% posso incluir dados em uma lista que esta dentro de uma tupla

tupla_rafa[-1].append("Londrina")
tupla_rafa

# %% 