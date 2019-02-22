import PySimpleGUI as sg
import mod as m
import view as v


apostas = m.getApostas()
coluna1 = [
    [sg.Button('Nova Aposta', key = 'adicionar',size=(15,1),  border_width= 1)],
    [sg.Button('Apagar Aposta', key = 'apagar',size=(15,1))],
    [sg.Button('Conferir Aposta', key = 'conferir',size=(15,1))],
    [sg.Listbox(values = '', size=(35,10), key = '',change_submits=True)],
    [sg.Button('Sair', size=(10,1))],
]
coluna2 = [
        [sg.Listbox(values = apostas, size=(100,100), key = 'listaAposta',change_submits=True)]
        ]
layout = [
            [sg.Column(coluna1,size=(500,500)) , sg.Column(coluna2, size=(600,400))],
        ]

janela = sg.Window('Lotomania', size=(900, 600), font=('Helvetica', 14)).Layout(layout)


while True:
    evento, valores = janela.Read()
    if evento == 'adicionar':
        aposta = v.dialogo_checkbox("Informe os 20 números da aposta", "Cadastro de apostas")
        r = m.nova_aposta(aposta)
        if r :
            sg.Popup('Aposta adicionada com sucesso!',font=('Helvetica', 14))
            ap = m.getApostas()
            janela.FindElement('listaAposta').Update(ap)
    if evento == 'apagar':
        aposta = valores['listaAposta'][0]
        r = v.dialogo_apagar()
        if r :
            m.apagarAposta(aposta)
            ap = m.getApostas()
            janela.FindElement('listaAposta').Update(ap)
        
        
    if evento == 'Sair' or evento is None:
        m.salvar_dados()
        janela.Close()
        break
