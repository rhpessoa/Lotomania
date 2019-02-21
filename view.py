import PySimpleGUI as sg
    
# dialogo que deve ser chamado quando se precisar marcar os numeros
def dialogo_checkbox(mensagem, titulo_janela):
    layout =  fabrica_checkbox(mensagem) # chama a fabrica de checkbox para criar o layout
    # mensagem é mensagem que vai no dialogo de checkbox
    window = sg.Window(titulo_janela).Layout(layout) # titulo é o titulo da janela
    evento, valores = window.Read()
    window.Close()
    if evento == 'ok':
        resposta = ler_numeros(valores) # se ok for pressionado chama o ler numeros
        #sg.Popup('Aposta adicionada com sucesso!',font=('Helvetica', 14))
        return resposta
 
# usando o padrao de projetos 
def fabrica_checkbox(mensagem):
    layout=[] # layout que vai ser retornado para compor a janela de dialogo
    num = 1
    layout.append([sg.Text(mensagem)])#antes de mais nada coloca uma mensagem como primeira linha do layout
    for linhas in range(10): # 10 linhas
        tmp=[]
        for i in range(10): # por 10 colunas = 100 numeros
            cb = sg.Checkbox(str('%02d'%(num))) # um checkbox com o numero fomatado para alinhamento ficar legal
            num +=1
            tmp.append(cb) # estamos adicionando cada checkbox ate formar uma linha
        layout.append(tmp) # linha completa adicionada ao layout

    layout.append([sg.Button('ok'), sg.Button('cancel')]) # adicionar dois botões ao final do layout
    return(layout)
 
def ler_numeros( resposta ):
    numeros =[]
    num = 1
    for r in resposta:
        if r == True:
            numeros.append(num)
        num = num + 1
    return numeros

def dialogo_apagar():
    layout = [[sg.Text('Apagar contato')],      
              [sg.Text('Voce tem certeza que deseja apagar o contato?')],
              [sg.Button('Confirmar'), sg.Cancel()]]      

    window = sg.Window('Apagar Contato',size=(300, 200), font=('Helvetica', 14)).Layout(layout)    

    event, values = window.Read()
    window.Close()
    if event == 'Confirmar':
        return True
    else:
        False

