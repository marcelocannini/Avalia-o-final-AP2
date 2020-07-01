import PySimpleGUI as gui
from Agente import Agente

class FormAgente:
    def __init__(self):
        conteudo = [
            [ gui.Text("Nome: "), gui.Input () ] ,
            [ gui.Text("CNPJ: "), gui.Input (key = 'txtCNPJ') ] ,
            [ gui.Button("Salvar") ]
        ]
        self.tela = gui.Window("Formulário de Agente").layout( conteudo )

    def show(self):
        self.button , self.valores = self.tela.Read()
        prod = Produto()
        prod.nome = self.valores [0]
        preco = self.valores ['CNPJ']

        return prod

