'''
    Projeto: Lotomania

1 - Descrição: Um programa para guardar apostas e verificá-las a partir de um input de resultado

2 - Modulos externos utilizados no projeto:
 PySimpleGUI - https://pysimplegui.readthedocs.io/

3 - Descricao do componente: componente princial que guarda a descricao da Interface grafica com o
    usuario

Autores: Cayo Araujo - Matrícula: 2018000000 - email@gmail.com
         Daniel Bahia Pinheiro - Matrícula: 2018001530- booude@gmail.com
         Felipe Moraes - Matrícula: 2018000000 - email@gmail.com
         Gabriel Carvalho - Matrícula: 2018000000 - email@gmail.com
         Rafael Henrique Pessoa - Matrícula: 2018004747 - rhpessoa29@gmail.com
         Yuri da Penha Ferreira - Matrícula: 2018005314 - yferreira30@gmail.com
versao : alpha 0.6

4 - Descrição dos arquivos do projeto:
- main.py - Aquivo principal que contem a interface grafica com o usuario

- mod.py - Arquivo de suporte com as funcoes do software relacionadas ao modelo, contem também a
estrutura de armazenamento, uma lista de dicionarios chamada APOSTAS

- view.py : Arquivo que contem os dialogos de suporte da aplicacao que auxiliam as operacoes
de entrada de nova aposta, remover aposta, etc.

- apostas.bin : Arquivo binario que guardas os dados da aplicação
'''
import PySimpleGUI as sg
import mod as m
import view as v

APOSTAS = m.get_apostas()
LOTERIAS = m.get_loteria()

sg.SetOptions(background_color='#f0f0f0',
              text_element_background_color='#f0f0f0',
              element_background_color='#f0f0f0',
              input_elements_background_color='#F7F3EC',
              button_color=('#f0f0f0', '#475841'),
              font='Helvetica',
              border_width=5)

COLUNA1 = [
    [sg.Button('Nova Aposta', key='adicionar', size=(15, 1))],
    [sg.Button('Apagar Aposta', key='apagar', size=(15, 1))],
    [sg.Button('Números Sorteados', key='sorteados', size=(15, 1))],
    [sg.Button('Conferir Aposta', key='conferir', size=(15, 1))],
    [sg.Text('', key='listaResultado', size=(20,3))],
    [sg.Button('Sair', size=(10, 1))],
]

COLUNA2 = [
        [sg.Listbox(values=APOSTAS, size=(70, 11), key='listaAposta', change_submits=True)]
        ]

LAYOUT = [
        [sg.Column(COLUNA1, size=(None, None), background_color='#f0f0f0'),
         sg.Column(COLUNA2, size=(None, None), background_color='#f0f0f0')]
        ]

JANELA = sg.Window('Lotomania', size=(880, 360), font=('Helvetica', 14)).Layout(LAYOUT)

while True:
    EVENTO, VALORES = JANELA.Read()
    if EVENTO == 'adicionar':
            APOSTA = v.dialogo_checkbox("Cadastro de apostas")
            R = m.nova_aposta(APOSTA)
            while R is False:
                sg.Popup('Por favor, escolha de 1 a 20 números!', font=('Helvetica', 14))
                APOSTA = v.dialogo_checkbox("Cadastro de apostas")
                R = m.nova_aposta(APOSTA)
            if R:
                sg.Popup('Aposta adicionada com sucesso!', font=('Helvetica', 14))
                AP = m.get_apostas()
                JANELA.FindElement('listaAposta').Update(AP)
                APOSTAS = AP

    if EVENTO == 'sorteados':
        RESULTADO = v.dialogo_checkbox("Cadastro de resultado")
        R = m.novo_resultado(RESULTADO)
        if R:
            sg.Popup('Resultado adicionado!', font=('Helvetica', 14))
            LOTERIAS = m.get_loteria()

    if EVENTO == 'conferir':
        APOSTA = VALORES['listaAposta'][0]
        LOTERIA = LOTERIAS[0]
        R = m.conferir_resultado(APOSTA, LOTERIA)
        JANELA.FindElement('listaResultado').Update('Você acertou {} número(s)'.format(len(R)))

    if EVENTO == 'apagar':
        APOSTA = VALORES['listaAposta'][0]
        R = v.apagar_aposta()
        if R:
            m.apagar_aposta(APOSTA)
            AP = m.get_apostas()
            JANELA.FindElement('listaAposta').Update(AP)
            JANELA.FindElement('listaResultado').Update('')

    if EVENTO == 'Sair' or EVENTO is None:
        m.salvar_dados()
        JANELA.Close()
        break
    