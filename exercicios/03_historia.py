# %% crie uma história interativa onde o usuário faz escolhas que afetam o desenrolar da narrativa.
print("Bem-vindo à aventura interativa!")
nome = input("Qual é o seu nome, aventureiro? ")
p1 = input("Você está em uma floresta misteriosa. Você vê uma trilha que se divide em duas direções. Qual você escolhe? (esquerda/direita): ")

p2 = input("Você escolheu ir para a " + p1 + ". Agora você vê uma caverna escura à sua frente. Você entra ou continua pela trilha? (entrar/continuar): ")

p3 = input("Enquanto você " + ("entra na caverna" if p2 == "entrar" else "continua pela trilha") + ", você encontra um objeto brilhante. Você pega o objeto ou o ignora? (pegar/ignorar): ")
