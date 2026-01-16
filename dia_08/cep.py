# %% como trabalhar com as APIS sda

import requests
import json
from tqdm import tqdm

import pandas as pd
# %% como consultar a dasdfgcvsd

ceps = [
    "01001000", "20040002", "30140071", "70040900", "80010000",
    "88010001", "90010000", "69005010", "40010000", "64000000",
    "65010000", "66010000", "59010000", "50010000", "57010000",
    "58010000", "49010000", "74003010", "78005010", "76801144"
]

url = "https://viacep.com.br/ws/{cep}/json/"

dados = []

for i in tqdm(ceps):

    resposta = requests.get(url.format(cep=i))
    dados.append(resposta.json())
    
dados
# %%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

# %% 

print(dados)

with open("ceps.json", "w", encoding="utf-8") as open_file:
    json.dump(dados,open_file, ensure_ascii=False, indent=4)

# %%