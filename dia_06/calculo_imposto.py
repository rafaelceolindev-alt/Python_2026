# %% criar uma função para calcular o imposto do produto sendo dois valores obrigatorios: preço e taxa de imposto usando **kwargs para taxas adicionais de imposto

def calcular_imposto(preco: float, taxa_imposto: float, **kwargs):
    imposto = preco * taxa_imposto
    
    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    return imposto

impostos_adicionais = {
    "municipal": 0.01,
    "estadual": 0.005,
    "federal": 0.001
}

calcular_imposto(100, 0.3, **impostos_adicionais) 

# %% 

