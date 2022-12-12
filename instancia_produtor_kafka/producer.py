from kafka import KafkaProducer
import random
from datetime import datetime
import time
from const import *
import sys
import json 


"""Simulando notificacao de um equipamento que monitora a cada 30 segundos as condicoes
 de temperatura uma sala de servidores """

"""
Definicao da mensagem (JSON):
{
 "id": "0",
 "data": "yyyy-MM-dd HH:mm:ss",
 "localizacao": "string",
 "valor": "99.99"
}
"""
def gerarDado():
    data = datetime.now()
    temperatura = round(random.uniform(-10.00, 45.99), 2)
    dado = {
        "data": data.strftime("%d/%m/%Y %H:%M:%S"),
        "id": idSensor,
        "localizacao": salaSensor,
        "valor": temperatura
    }
    msg = json.dumps(dado)
    return msg
    

if __name__ == '__main__':
    n = len(sys.argv)
    idSensor = sys.argv[1] if(n > 0) else 1
    
    topico = 'temperatura'
    salaSensor = 'Sala ' + str(idSensor)
    producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])

    while True:
        msg = gerarDado()
        print(msg)
        producer.send(topico, value=msg.encode())
        time.sleep(30)

    producer.flush()