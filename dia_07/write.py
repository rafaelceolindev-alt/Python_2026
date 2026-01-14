# %% aqui estamos escrevendo em um arquivo de texto onde W significa write (escrever) sobrescreve o arquivo se ele já existir e se usarmos A (append) ele adiciona ao final do arquivo

txt = "esqueci o que ia escrever"
nome_arquivo = 'historia.txt'
with open(nome_arquivo, mode="w") as open_file:
    open_file.write(txt)

# %%
txt = "esqueci o que ia escrever"
nome_arquivo = 'historia.txt'
with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)