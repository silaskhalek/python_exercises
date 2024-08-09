# Faça um programa que peça ao usuário para digitar um número inteiro, \
# informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, 
# informe que não é um número inteiro. 

nome = input('Digite o seu nome: ')
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'Olá, {nome}. O {numero} que você digitou é um número par.')
else:
    print(f'Olá, {nome}. O número {numero} que você digitou é um número ímpar.')
