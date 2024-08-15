while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numero_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operados_permitidos = '+-/*'

    if operador not in operados_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Estamos realizando a sua conta... Aguarde um momento.')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float * num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    else:
        print('Error 404.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        print('Esperamos ter você de volta em breve!')
        break