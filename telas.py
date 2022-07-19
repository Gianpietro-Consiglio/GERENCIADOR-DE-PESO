import PySimpleGUI as psg

def Tela_Principal():
    psg.theme("DarkGrey14")
    layout = [
        [psg.Button('Inserir dados do dia', font="Verdana")],
        [psg.Button('Ver informações', font="Verdana")]
    ]

    return psg.Window('Menu',layout=layout,finalize=True,element_justification='c')


def Tela_Dados():
    psg.theme("DarkGrey14")
    layout = [
        [psg.Text('Altura:',font='Verdana'),psg.Input(key='altura')],
        [psg.Text('Peso:',font='Verdana'),psg.Input(key='peso')],
        [psg.Button('Cadastrar',font='Verdana'),psg.Button('Voltar',font='Verdana')]
    ]
       

    return psg.Window('Informações do dia',layout=layout,finalize=True, element_justification='c')

def Tela_Informacoes():
    psg.theme("DarkGrey14")
    layout = [
         [psg.Output(size=(50,20),background_color='Black',text_color='White',font='Verdana',key='mensagem')],
         [psg.Button('Buscar',font='Verdana'), psg.Button('Voltar',font='Verdana')]
    ]

    return psg.Window("Informações gerais",layout=layout,finalize=True, element_justification='c')
