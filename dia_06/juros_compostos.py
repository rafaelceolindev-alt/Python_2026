# %% funçao para juros compostos com parâmetros e documentação 

def juros_compostos(principal:int, taxa:float, tempo:int) -> float:
    """
    Esta função calcula o montante acumulado com juros compostos.
    :param principal: Valor inicial investido
    :param taxa: Taxa de juros (em decimal, por exemplo, 0.13 para 13%)
    :param tempo: Tempo em anos
    """
    montante = principal * (1 + taxa) ** tempo
    return montante

print(juros_compostos(principal=int(input("Digite o valor principal: ")), taxa=0.13, tempo=4))  # Exemplo de uso da função