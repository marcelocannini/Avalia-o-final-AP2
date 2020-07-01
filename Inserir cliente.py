#from conexao import Conexao
import mysql.connector
from FormCliente import FormCliente
from Cliente import Cliente

form = FormCliente()
cliente = form.show()

conn = mysql.connector.connect(host = 'localhost', database = 'loja_ap2', user = 'root', password = '')
if conn.is_connected():
    print("Conectado!")

cursor = conn.cursor()


query = "INSERT INTO clientes (nome, sexo, idade, telefone, altura, peso, imc, objetivo_cliente, imc_observacao, convenio) VALUES ("
query += " '"+cliente.nome+" ', '" + cliente.sexo + "' , " + str(cliente.idade) + " ,  ' "+cliente.telefone+" ' , "+ str(cliente.altura)+", "+ str(cliente.peso)+", "+ str(cliente.imc)+" , '"+ cliente.objetivo_cliente +"' , '"+ cliente.imc_observacao +"' , '"+cliente.convenio+"') "

print (cliente.convenio)

cursor.execute(query)

conn.commit()