nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Sua idade é {idade} anos.')
    print(f'Seu nome invertido é {nome[::-1]}.')

    if " " in nome:
        print(f'Seu nome contém espaços.')
    else:
        print(f'Seu nome não contém espaços.')

    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}.')
    print(f'A última letra do seu nome é {nome[-1]}.')

    
else:
    print('Desculpe, você deixou campos vazios.')

