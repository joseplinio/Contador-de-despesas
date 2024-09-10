from datetime import datetime
import json

#    Função que cria uma linha
def linha(msg=42):
    return msg*'_'

#   Cria um cabeçario usando a def linha
def cabeçario(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

#   Cria um menu usando a def linha e cabeçario, mas também usa um for pra uma lista é a inumera assim criando o menu
def menu(lista):
    cabeçario('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção\033[m: ')
    return opc

#   Função que verifica o número inteiro antes de pegar os dados
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

#   Função que verifica o número float antes de pegar os dados
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

#   Função que valida a formataçao da data e sua validade (usa a biblioteca datetime, tive ajuda do chat GTP nessa drf) 
def valida_data(data_str):
    try:
        return datetime.strptime(data_str,'%d/%m/%Y')
    except ValueError:
        print('\033[31mData inválida! Use o formato DD/MM/AAAA.\033[m')
        return None

#   Função que salva as despesas em arquivo .txt e os salva nesse aquivo de forma formatada:
def salvar_despesa(despesa, nome_arquivo='despesa.txt'):
    """
    A def salvar_despesa usa dois parametros [despesa, nome_arquivo = "despesa.txt"]
    a def tenta abrir o arquivo colocando as informaçoes no arquivo usando o metedo "a"
    para escrever a despesa de forma formatada e garante que o arquivo e fechado logo depois do uso,
    ele tambem retorna a user o erro caso tenha dado um.
    """
    try:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f'{despesa.data} - {despesa.valor} - {despesa.categoria}\n')
        print(f'\033[32mDespesas salvas com sucesso em  {nome_arquivo}\033[m.')
    except Exception as e:
        print(f'\033[31mErro ao salvar despesas: {e}\033[m')