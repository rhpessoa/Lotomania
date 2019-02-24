'''
Arquivo de suporte com as funcoes do software relacionadas ao modelo, contem também a
estrutura de armazenamento , uma lista de dicionarios chamada APOSTAS
'''
import pickle

APOSTAS = [{'aposta':[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]}]
LOTERIA = [1, 2, 3, 4, 5]

def get_apostas():
    '''
        Função para enviar valores das apostas ao main
    '''
    apostas = []
    for aposta in APOSTAS:
        apostas.append(aposta['aposta'])
    return apostas

def nova_aposta(aposta):
    '''
        Função para adicionar nova aposta
    '''
    APOSTAS.append({'aposta':aposta})
    return True

def apagar_aposta(aposta):
    '''
        Função para apagar as apostas individualmente através da seleção na listbox
    '''
    for _ap in APOSTAS:
        if _ap['aposta'] == aposta:
            APOSTAS.remove(_ap)

def salvar_dados():
    '''
        Salvar os dados com pickle em um arquivo binário
    '''
    with open('apostas.bin', 'wb') as arquivo:
        pickle.dump(APOSTAS, arquivo)
        return 0

def carregar_dados():
    '''
        Carregar os dados com pickle de um arquivo binário
    '''
    tmp = []
    try:
        with open('apostas.bin', 'rb') as arquivo:
            tmp = pickle.load(arquivo)
            for _a in tmp:
                APOSTAS.append(_a)
        return 0
    except FileNotFoundError:
        print('Error sei la')

def conferir_resultado(resultado):
    '''
        Tentativa de implementar verificação de resultado
    '''
    match = []
    for i in resultado:
        for j in LOTERIA:
            if i == j:
                match.append(i)
    return match
