'''
    Arquivo que contém os diálogos de suporte da aplicação que auxiliam as operações
    de entrada de nova aposta, remover aposta, etc.
'''
import PySimpleGUI as sg
import mod as m

def dialogo_checkbox(mensagem):
    '''
        Diálogo que deve ser chamado quando se precisar marcar os numeros

        layout = fabrica_checkbox(mensagem)
            Chama a fábrica de checkbox para criar o layout
            Mensagem é a mensagem que vai no diálogo de checkbox

        resposta = m.ler_numeros(valores)
            Se ok for pressionado chama o ler números
    '''
    layout = fabrica_checkbox(mensagem)
    janela = sg.Window('Informe os 20 números da aposta').Layout(layout)
    evento, valores = janela.Read()
    janela.Close()
    if evento == 'Confirmar':
        resposta = m.ler_numeros(valores)
        return resposta
    if evento == 'Cancelar':
        return -1
    return None

def fabrica_checkbox(mensagem):
    '''
        Usando o padrão de projetos

        layout = []
            Layout que vai ser retornado para compor a janela de diálogo

        layout.append([sg.Text(mensagem)])
            Antes de mais nada coloca uma mensagem como primeira linha do layout

        cb = sg.Checkbox(str('%02d'%(num)))
            Um checkbox com o numero fomatado para alinhamento ficar legal

        tmp.append(checkbox)
            Estamos adicionando cada checkbox até formar uma linha

        layout.append(tmp)
            Linha completa adicionada ao layout

        layout.append([sg.Button('Confirmar', size=(10, 1)), sg.Button('Cancelar')])
            Adicionar dois botões ao final do layout
    '''
    layout = []
    num = 1
    layout.append([sg.Text(mensagem)])
    for _ in range(10):
        tmp = []
        for _ in range(10):
            checkbox = sg.Checkbox(str('%02d'%(num)))
            num += 1
            tmp.append(checkbox)
        layout.append(tmp)
    layout.append([sg.Button('Confirmar', size=(10, 1)), sg.Button('Cancelar', size=(10, 1))])
    return layout

def apagar_aposta():
    '''
        Função para mostrar o diálogo de apagar aposta
    '''
    layout = [[sg.Text('Apagar aposta')],
              [sg.Text('Voce tem certeza que deseja apagar a aposta?')],
              [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]

    janela = sg.Window('Apagar aposta', size=(400, 125), font=('Helvetica', 12)).Layout(layout)

    evento, _ = janela.Read()
    janela.Close()
    if evento == 'Confirmar':
        return True
    return None
