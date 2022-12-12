from kafka import KafkaConsumer
from const import *
from datetime import datetime
import sys
import json
import mariadb

"""
Definicao da mensagem (JSON):
{
 "id": "0",
 "data": "yyyy-MM-dd HH:mm:ss",
 "localizacao": "string",
 "valor": "99.99"
}
"""

topico = 'temperatura'

def getConnection():
    try:
        conn = mariadb.connect(
            user="root",
            password="root",
            host="localhost",
            port=3306,
            database="sensor"

        )
        
        return conn
    except mariadb.Error as e:
        print(f"Erro ao se conectar ao banco: {e}")
        sys.exit(1)

def decodeMessage(msg : str):
    dados = json.loads(msg)
    return dados

def persistirDados(dados : dict):
    sql = 'INSERT INTO DadosSensores (data, id_sensor, localizacao, valor) VALUES (?, ?, ?, ?)'
    conn = getConnection()
    cursor = conn.cursor()
    data = datetime.strptime(dados['data'], '%d/%m/%Y %H:%M:%S')
    cursor.execute(sql, (data, dados['id'], dados['localizacao'], dados['valor'],))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    consumer = KafkaConsumer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])
    consumer.subscribe([topico])
    for msg in consumer:
        print(msg.value.decode())
        dados  = decodeMessage(msg.value.decode())
        persistirDados(dados)