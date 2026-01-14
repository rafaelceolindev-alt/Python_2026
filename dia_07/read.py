# %% 7.1 - Lendo arquivos de texto

nome_arquivo = "historia.txt"

open_file = open(nome_arquivo)

conteudo = open_file.read()

# %% 7.2 - Exibindo o conteúdo do arquivo

print(conteudo)

# %% 7.3 - Fechando o arquivo

open_file.close()

# %% a forma acima não é a mais recomendada para ler arquivos. O ideal é usar o gerenciador de contexto "with", pois ele garante que o arquivo será fechado corretamente após o uso, mesmo que ocorra um erro durante a leitura.

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
    print(conteudo)