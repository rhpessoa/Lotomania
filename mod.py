import pickle
APOSTAS = [{'aposta':[1,2,3,4,5,6,18,19,20]}]

def getApostas():
    apostas = []
    for aposta in APOSTAS:
        apostas.append(aposta['aposta'])
    return apostas


def nova_aposta(aposta):
    '''
    função para adicionar nova aposta
    '''
    APOSTAS.append({'aposta':aposta})
    return True

def apagarAposta(aposta):
    for ap in APOSTAS:
        if ap['aposta'] == aposta:
            APOSTAS.remove(ap)
    
    
def salvar_dados():
    with open('apostas.bin', 'wb') as arquivo:
        pickle.dump(APOSTAS, arquivo)
        return 0

def carregar_dados():
    tmp = []
    try:
        with open('apostas.bin', 'rb') as arquivo:
            tmp = pickle.load(arquivo) 
            for a in tmp:
                APOSTAS.append(a)
        return 0
    except FileNotFoundError:
        print('Error sei la')