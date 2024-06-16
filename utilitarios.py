from datetime import datetime

def linha(msg=42):
    return msg*'_'

def cabeçario(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! insira dados validos!\033[m')
        except KeyboardInterrupt:
            print('\033[31mERRO! osúario não informou os dados!\033[m')
        else:
            return n

def menu(lista):
    cabeçario('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção\033[m: ')
    return opc

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! insira dados validos!\033[m')
        except KeyboardInterrupt:
            print('\033[31mERRO! usúario não informou os dados!\033[m')
        else:
            return n
    
def valida_data(data_str):
    try:
        return datetime.strptime(data_str,'%d/%m/%Y')
    except ValueError:
        print('\033[31mData inválida! Use o formato DD/MM/AAAA.\033[m')
        return None