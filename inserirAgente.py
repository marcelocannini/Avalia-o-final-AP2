#from conexao import Conexao
import mysql.connector
from FormAgente import FormAgente

form = FormAgente()
agente = form.show ()

conn = mysql.connector.connect(host = 'localhost', database = 'loja_ap2', user = 'root', password = '')
if conn.is_connected():
    print("Conectado!")

cursor = conn.cursor()

query = "INSERT INTO agente (nome, cnpj) VALUES ("
query += " '"+agente.nome+"', "+agente.cnpj+") "

cursor.execute(query)

conn.commit()