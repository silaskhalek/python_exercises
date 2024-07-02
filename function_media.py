
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f'A soma dos elementos é {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

lista_valores = [15,20,25,30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor 
    media = soma_valores / len(lista_valores)
    print(f'Média dos valores é: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')


