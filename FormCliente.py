import PySimpleGUI as gui
from Cliente import Cliente

import mysql.connector

conn = mysql.connector.connect(host = 'localhost', database = 'loja_ap2', user = 'root', password = '')
if conn.is_connected():
    cursor = conn.cursor()

cursor.execute("SELECT nome FROM agente")

result = cursor.fetchall()
out = list(sum(result, ()))
result = out

class FormCliente:
    def __init__(self):
        conteudo = [
            [ gui.Text("Nome: "), gui.Input (size=(20,10), key = 'txtNome') ] ,
            [
                gui.Text("Sexo "),
                gui.Radio ("Feminino", 'sexo', key = 'feminino') , gui.Radio("Masculino", ' sexo', key = 'masculino')
            ] ,
            [gui.Text("Idade: "), gui.Slider(range =(0,110), orientation = 'h', key = 'idade', default_value = 18)],
            [gui.Text("Telefone: "), gui.Input(size=(20, 10) ,key='txtTelefone')],
            [gui.Text("Altura (Metros): "), gui.Input(size=(20, 10), key='txtAltura')],
            [gui.Text("Peso (Kg): "), gui.Input(size=(20, 10), key='txtPeso')],
            [gui.Text("Objetivo físico: "), gui.InputCombo(('Emagrecimento','Condicionamento','Hipertrofia'), size = (30,3), key = 'txtObj') ],

            [gui.Text("Convenios: "), gui.InputCombo((result), size=(30, 3), key='txtConvenio')],

            [gui.Button("Enviar")]

        ]
        self.tela = gui.Window("Formulário de Cliente").layout( conteudo )

    def show(self):
        self.button, self.valores = self.tela.Read()
        cliente = Cliente()
        cliente.nome = self.valores['txtNome']
        cliente.nome = self.valores['txtNome']
        if self.valores['feminino']:
            cliente.sexo = 'feminino'
        elif self.valores ['masculino']:
            cliente.sexo = 'masculino'
        else:
            cliente.sexo = "Não informado"

        cliente.idade = self.valores['idade']
        cliente.telefone = self.valores['txtTelefone']
        altura = self.valores['txtAltura']
        altura = float(altura.replace(",", "."))
        cliente.altura = altura
        peso = self.valores['txtPeso']
        peso = float(peso.replace(",", "."))
        cliente.peso = peso

        imc = (peso / (altura * altura))
        imc = round (imc, 1)

        cliente.imc = imc
        if cliente.imc < 18.50:
            cliente.imc_observacao = "Abaixo do peso"
        elif  18.5 <= cliente.imc < 25:
            cliente.imc_observacao = "Peso ideal"
        elif  25 <= cliente.imc < 30 :
            cliente.imc_observacao = "Levemente acima do peso"
        elif  30 <= cliente.imc < 35:
            cliente.imc_observacao = "Obesidade Grau I"
        elif 35 <= cliente.imc < 40:
            cliente.imc_observacao = "Obesidade Grau II"
        elif cliente.imc > 40:
            cliente.imc_observacao = "Obesidade Grau III (Mórbida)"
        else:
            cliente.imc_observacao = "Não informado"
        ###
        cliente.objetivo_cliente = self.valores['txtObj']
        cliente.convenio = self.valores['txtConvenio']


        return cliente


