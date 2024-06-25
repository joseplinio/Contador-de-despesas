from time import sleep
from utilitarios import *
from descricao import *
lista_de_despesas = []
while True:
    resp = menu(['Anotar despesas','Ver historico','Salvar despeses','Sair do sistema'])
    if resp == 1:
        #   Adicionar despesas do usuario, de fomar que cada um dos dados seja
        #   validados antes de entra para o banco de dados. 
        while True:
            sleep(1)   
            data = None
            while data is None:
                data= valida_data(input('\033[34mData (DD/MM/AAAA)\033[m:'))
            valor= leiafloat('\033[34mValor R$\033[m: ')
            categoria = input('\033[34mCategoria\033[m: ')
            despesas = Descricao(data.strftime('%d/%m/%Y'), valor, categoria)
            lista_de_despesas.append(despesas)
            print(linha())
            opc = ' '
            while opc not in 'sn':
                opc = str(input('\033[34mQuer continuar?\033[34m \033[32m[s/n]\033[m: ')).lower().strip()[0]
            if opc in 's':
                print(linha())
            if opc in 'n':
                break
    elif resp == 2:
        #   Mostra todas as despesas (formatada) de forma que o osuario entenda
        #   de forma dinamica sua despeas mensais, ou semanais
        if lista_de_despesas:
            cabeçario('\033[32mHistórico de Despesas\033[m:')
            for despesa in lista_de_despesas:
                print(despesa)
        else:
            print('\033[31mNenhuma despesa registrada\033[m.')
        input('\033[32mPressione Enter para continuar\033[m...') 
    elif resp == 3:
        #   Sistema pra salva todas as despessas colocadas, mas tambem com um
        #   sistema para que o usuario consiga escolher o que salve e juntamente
        #   apargar oque ele quer.
            lista_de_despesas
    elif resp == 4:
        #   Finaliza o programa
        cabeçario('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mERRO! digite uma opção valida\033[m')
        sleep(1)
