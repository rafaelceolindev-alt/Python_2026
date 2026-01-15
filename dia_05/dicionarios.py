# %% 

lista = [1, 2, 3, 4, 5]

lista[2]

# %% dicinarios sao pares chave-valor   podemos usar strings, numeros ou tuplas como chaves

dados_rafa = {
    "idade": 25,
    "cidade": "São Paulo", "profissao": "Engenheiro",
    "formacao": ["Mecatrônica", "Engenharia de Software"],
    "cargos": [
        {"nome": "Estagiário", "ano": 2015},
        {"nome": "Júnior", "ano": 2016},
        {"nome": "Pleno", "ano": 2018},
        {"nome": "Sênior", "ano": 2020},
    ],
}

# %% acessando valores do dicionario
print(dados_rafa)

print(dados_rafa["formacao"][-1])
print(dados_rafa["cargos"][-1]["ano"])

# %% adicionando novos pares chave-valor e consultando chaves

dados_rafa["estado_civil"] = "casado"

dados_rafa.keys()

# %% valores do dicionario
print("Valores: ", dados_rafa.values())
print("Chaves: ", dados_rafa.keys())
print("Itens: ", dados_rafa.items())

# %% for para iterar sobre dicionarios
for I in dados_rafa:
    print(I, "->", dados_rafa[I])

# %% usando itens() para iterar sobre chaves e valores

for item in dados_rafa.items():
    print(item)

#  %% desempacotando itens em chave e valor

for chave, valor in dados_rafa.items():
    print(chave, "->", valor)