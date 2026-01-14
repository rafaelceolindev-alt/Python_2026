# %% readlines() - Lê todas as linhas de um arquivo e retorna uma lista isso pode ser útil para processar o conteúdo linha por linha. sendo cada linha um registro.

arquivo = "data.csv"

with open(arquivo) as open_file:
    data = open_file.readlines()
    print(data)

for linha in data:
    print(linha) # Imprime cada linha do arquivo individualmente

# %% podemos criar uma estrutura de dados mais organizada, como uma lista de dicionários, onde cada dicionário representa um registro com chaves correspondentes aos nomes das colunas.

dados = dict()

chaves = data[0].strip("\n").split(";") # Extrai os nomes das colunas da primeira linha do arquivo e transforma em uma lista
for c in chaves:
    dados[c] = [] # Inicializa uma lista vazia para cada chave no dicionário

# %% Agora, vamos preencher o dicionário com os dados do arquivo, organizando-os por colunas.
for linha in data[1:]:
    valores = linha.strip("\n").split(";")
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])
     # Itera sobre as linhas do arquivo, ignorando a primeira linha (cabeçalho)
dados # Exibe o dicionário resultante com os dados organizados por colunas

# %% Agora, podemos acessar os dados de forma mais estruturada. Por exemplo, para obter todos os valores da coluna "idade":
idades = dados["idade"]
print(idades)  # Imprime a lista de idades

# %% ou ainda podemos obter a media das idades:
idades = []
for i in dados["idade"]:
    idades.append(int(i))

media_idade = sum(idades) / len(idades)
media_idade