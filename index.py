from time import sleep
from src.utilitarios import *
from src.descricao import *

while True:

    resp = menu(['Anotar despesas','Ver historico','Sair do sistema'])
    if resp == 1:
        #   Adicionar despesas do usuario: 
        
        while True:
            
            sleep(1)   
            data = None
            
            while data is None:
                data= valida_data(input('\033[34mData (DD/MM/AAAA)\033[m:'))
            valor= leiafloat('\033[34mValor R$\033[m: ')
            categoria = input('\033[34mCategoria\033[m: ')
            despesa = Descricao(data.strftime('%d/%m/%Y'), valor, categoria)
            
            salvar_despesa(despesa)
            print(linha())
            
            opc = ' '
            while opc not in 'sn':
                opc = str(input('\033[34mQuer continuar?\033[34m \033[32m[s/n]\033[m: ')).lower().strip()[0]
            if opc in 's':
                print(linha())
            if opc in 'n':
                break
    
    elif resp == 2:
        #   Mostra todas as despesas:
        cabeçario('\033[32mHistórico de Despesas\033[m:')
        try:
            with open("despesa.txt", "r") as arquivo_data:
                for despesa in arquivo_data:
                    print(f'\t{despesa}')

        except ValueError:
            print(f'\033[31mErro! O arquivo deve ser um str.\033[m')

        except FileNotFoundError:
            print('\033[31mNenhuma despesa registrada\033[m.')
        input('\033[32mPressione Enter para continuar\033[m...') 
    
    elif resp == 3:
        # Finaliza o programa:
        cabeçario('Saindo do sistema... até logo!')
        break
    
    else:
        print('\033[31mERRO! digite uma opção valida\033[m')
        sleep(1)
