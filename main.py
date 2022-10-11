# Menu App Collections
import coletasimples
def menu():
    while True:
        linha = '-'
        # Inicio Cabecalho
        print(f"{linha}" * 100)
        print(f"{linha}" * 42 + ' CollectionsApp ' + f'{linha}' * 42)
        print(f'{linha}' * 100)
        # Fim Cabecalho
        # Inicio Menu
        print(f' {"Menu" : ^99s}')
        print(f'{linha}' * 10 + ' 1 - Busca Simples ')
        print(f'{linha}' * 10 + ' 2 - Busca Médiana ')
        print(f'{linha}' * 10 + ' 3 - Busca Avançada ')
        print(f'{linha}' * 10 + ' 4 - Sair ')
        print(f'{linha}' * 100)
        opcao = str(input('Informe a opção desejada: '))
        # Fim Menu
        if opcao == '':
            print('Valor não pode ficar em branco, Tente Novamente! ')
        else:
            if opcao == '1':
                opcao_1()
            elif opcao == '2':
                opcao_2()
            elif opcao == '3':
                opcao_3()
            elif opcao == '4':
                break
            else:
                print('Opção Inválida, Tente Novamente! ')

def opcao_1():
    print('Busca Simples')
    coletasimples.alvo()

def opcao_2():
    print('Busca Médiana')


def opcao_3():
    print('Busca Avançada')


if (__name__ == "__main__"):
    menu()

