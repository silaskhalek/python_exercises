# Faça um programa que peça o primeiro nome do usuário. 
# Se o nome tiver 4 letras ou menos, escreva:
# seu nome é curto; 
# Se o nome tiver 5 ou 6 letras, escreva:
# seu nome é normal;
# Se o nome tiver 6 letras ou mais, escreva:
# seu nome é muito grande. 

nome = float(input('Qual o seu primeiro nome? '))
# nome_float = float(nome)

if (nome) <= 4:
    print(f'Seu nome é curto!')
elif (nome) > 5 and (nome) <= 6:
    print(f'Seu nome é normal/médio!')
else:
    print(f'Seu nome é muito grande!')

