'''
    Projeto: Lotomania

1 - Descrição: Um programa para guardar apostas da Lotomania (CAIXA) e verificá-las a partir
               de um input de resultado. Determina a quantidade de valores acertados por aposta
               e indica qual é a premiação de acordo com a CAIXA.

2 - Módulos externos utilizados no projeto:
    PySimpleGUI - https://pysimplegui.readthedocs.io/
    Numpy - http://www.numpy.org/

3 - Descricao do componente: Componente princial que guarda a descrição da interface gráfica com o
    usuário e acessa os componentes auxiliares.

Autores: Cayo Rodrigues Araujo  - Matrícula: 2018001549 - cayorodrigues15@gmail.com
         Daniel Bahia Pinheiro  - Matrícula: 2018001530 - booude@gmail.com
         Felipe Sousa de Moraes - Matrícula: 2018001600 - lipe-evo3@hotmail.com
         Gabriel Carvalho Pinto - Matrícula: 2018001502 - gabriel_carvalho_pinto@outlook.com
         Rafael Henrique Pessoa - Matrícula: 2018004747 - rhpessoa29@gmail.com
         Yuri da Penha Ferreira - Matrícula: 2018005314 - yferreira30@gmail.com

Versão : alpha 0.8

4 - Descrição dos arquivos do projeto:
- main.py - Arquivo principal que contém a interface gráfica com o usuário

- mod.py - Arquivo de suporte com as funções do software relacionadas ao modelo, contém também a
           estrutura de armazenamento, uma lista de dicionários chamada APOSTAS e uma outra lista
           chamada LOTERIAS para a realização de testes.

- view.py - Arquivo que contém os diálogos de suporte da aplicação que auxiliam as operações
            de entrada de nova aposta, remover aposta, etc.

- apostas.bin - Arquivo binário que guarda os dados da aplicação.
'''
import PySimpleGUI as sg
import mod as m
import view as v

m.carregar_dados()
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
    [sg.Text('', key='listaResultado', size=(22, 0))],
    [sg.Text('', key='premio', size=(22, 0))],
    [sg.Button('Sair', size=(10, 1))],
]

COLUNA2 = [
        [sg.Listbox(values=APOSTAS, size=(75, 11), key='listaAposta', change_submits=True)]
        ]

LAYOUT = [
        [sg.Column(COLUNA1, size=(None, None), background_color='#f0f0f0'),
         sg.Column(COLUNA2, size=(None, None), background_color='#f0f0f0')]
        ]

JANELA = sg.Window('Lotomania', size=(900, 360), font=('Helvetica', 14)).Layout(LAYOUT)

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
        while R is False:
            sg.Popup('Por favor, escolha 20 números!', font=('Helvetica', 14))
            RESULTADO = v.dialogo_checkbox("Cadastro de resultado")
            R = m.novo_resultado(RESULTADO)
        if R:
            sg.Popup('Resultado adicionado!', font=('Helvetica', 14))
            LOTERIAS = m.get_loteria()

    if EVENTO == 'conferir':
        try:
            APOSTA = VALORES['listaAposta'][0]
            LOTERIA = LOTERIAS[0]
            R = m.conferir_resultado(APOSTA, LOTERIA)
            JANELA.FindElement('listaResultado').Update('Você acertou {} número(s)'.format(len(R)))
            if len(R) == 20:
                JANELA.FindElement('premio').Update('Você ganhou R$:585.000,00')
            elif len(R) == 19:
                JANELA.FindElement('premio').Update('Você ganhou R$:208.000,00')
            elif len(R) == 18:
                JANELA.FindElement('premio').Update('Você ganhou R$:130.000,00')
            elif 17 >= len(R) >= 15:
                JANELA.FindElement('premio').Update('Você ganhou R$:91.000,00')
            elif not R:
                JANELA.FindElement('premio').Update('Você ganhou R$:104.000,00')
            else:
                JANELA.FindElement('premio').Update('Boa sorte na próxima vez')
        except IndexError as _e:
            sg.Popup('''Erro "{}"
Selecione uma aposta da lista.''' .format(_e), font=('Helvetica', 14))

    if EVENTO == 'apagar':
        try:
            APOSTA = VALORES['listaAposta'][0]
            R = v.apagar_aposta()
            if R:
                m.apagar_aposta(APOSTA)
                AP = m.get_apostas()
                JANELA.FindElement('listaAposta').Update(AP)
                JANELA.FindElement('listaResultado').Update('')
                JANELA.FindElement('premio').Update('')
        except IndexError as _e:
            sg.Popup('''Erro "{}"
Selecione uma aposta da lista.''' .format(_e), font=('Helvetica', 14))

    if EVENTO == 'Sair' or EVENTO is None:
        m.salvar_dados()
        break
JANELA.Close()
