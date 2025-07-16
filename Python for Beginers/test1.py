'''
crie uma função que simule um sistema de reservas de um cinema. a função deve RECEBER uma lista de dicionários 
de todas as cadeiras indicando se estão reservadas ou não, e o seu número e uma lista de acentos a serem reservados
pelo usuário a função deve retornar a lista atualizada de todas as cadeiras após as reservas serem feitas e deve 
mostrar uma mensagem de erro para cada tentativa de reserva em um acento ja reservado
'''


lista_cadeiras = [{'numero':1, 'reserva':False}, 
                  {'numero':2, 'reserva':True},
                  {'numero':3, 'reserva':False},
                  {'numero':4, 'reserva':True}]

def cinema(reservas, lista_cadeiras):
    for numero_assento in reservas:
        cadeira_correspondente = False #cria uma variavel de controle
        for cadeira in lista_cadeiras: 
            if cadeira['numero'] == numero_assento:
                cadeira_correspondente = cadeira
                break
        if cadeira_correspondente == False:
            print(f'Cadeira {numero_assento} não existe')
        elif cadeira_correspondente['reserva']:
            print(f'Cadeira {numero_assento} reservado')
        else:
            cadeira_correspondente['reserva'] = True
            print(f'reserva confirmada para o assento {numero_assento}')
    return lista_cadeiras

reserva_lista = list(map(int, input('insira o numero das cadeiras a serem reservadas: ').split()))

print(cinema(reserva_lista, lista_cadeiras))