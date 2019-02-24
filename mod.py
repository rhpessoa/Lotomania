'''
    Arquivo de suporte com as funções do software relacionadas ao modelo, contém também a
    estrutura de armazenamento, uma lista de dicionários chamada APOSTAS e uma outra lista
    chamada LOTERIAS para a realização de testes.
'''
import pickle

APOSTAS = [{'aposta':[10, 30, 40, 50, 60, 70, 80, 90, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]}]
LOTERIAS = [{'resultado':[1, 2, 3, 4, 5]}]

def get_apostas():
    '''
        Função para enviar valores das apostas ao main
    '''
    apostas = []
    for valor in APOSTAS:
        apostas.append(valor['aposta'])
    return apostas

def get_loteria():
    '''
        Função para enviar valores dos resultados ao main
    '''
    loteria = []
    for valor in LOTERIAS:
        loteria.append(valor['resultado'])
    return loteria

def nova_aposta(aposta):
    '''
        Função para adicionar nova aposta
    '''
    if aposta == -1:
        pass
    elif aposta is False:
        return False
    else:
        APOSTAS.append({'aposta':aposta})
        return True
    return None

def novo_resultado(resultado):
    '''
        Função para adicionar novo resultado
    '''
    if resultado == -1:
        pass
    elif resultado is False:
        return False
    else:
        del LOTERIAS[:]
        LOTERIAS.append({'resultado':resultado})
        return True
    return None

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

def conferir_resultado(resultado, loteria):
    '''
        Verificação de resultado
    '''
    match = []
    for i in resultado:
        for j in loteria:
            if i == j:
                match.append(i)
    return match

def ler_numeros(resposta):
    '''
        Módulo auxiliar da fábrica de checkbox
    '''
    numeros = []
    num = 1
    for _r in resposta:
        if _r is True:
            numeros.append(num)
        num += 1
    if not numeros or len(numeros) > 20:
        return False
    return numeros
