import grpc
from concurrent import futures
import mariadb
import sys
from datetime import datetime
import SensorService_pb2
import SensorService_pb2_grpc

class SensorServer(SensorService_pb2_grpc.SensorServiceServicer):
    def ConsultarListaPorLocalizacao(self, request, context):
        conn = getConnection()
        sql = "SELECT * FROM DadosSensores WHERE localizacao=?"
        cur = conn.cursor()
        cur.execute(sql, (request.localizacao,))
        listaDadosRetorno = SensorService_pb2.ListaDados()
        for id, data, id_sensor, localizacao, valor in cur:
            dadoRetorno = SensorService_pb2.Dado(id=id, data=data.strftime("%d/%m/%Y, %H:%M:%S"), localizacao=localizacao, valor=valor)
            listaDadosRetorno.dados.append(dadoRetorno)
        conn.close()    
        return listaDadosRetorno
        
    def ConsultarListaPorData(self, request, context):
        conn = getConnection()
        sql = "SELECT * FROM DadosSensores WHERE date(data)=?"
        cur = conn.cursor()
        dataConvertida = datetime.strptime(request.data, '%d/%m/%Y')
        cur.execute(sql, (dataConvertida,))
        listaDadosRetorno = SensorService_pb2.ListaDados()
        for id, data, id_sensor, localizacao, valor in cur:
            dadoRetorno = SensorService_pb2.Dado(id=id, data=data.strftime("%d/%m/%Y, %H:%M:%S"), localizacao=localizacao, valor=valor)
            listaDadosRetorno.dados.append(dadoRetorno)
        conn.close()    
        return listaDadosRetorno
        
    def ConsultarListaPorDataELocalizacao(self, request, context):
        conn = getConnection()
        sql = "SELECT * FROM DadosSensores WHERE localizacao=? and date(data)=?"
        cur = conn.cursor()
        dataConvertida = datetime.strptime(request.data.data, '%d/%m/%Y')
        cur.execute(sql, (request.local.localizacao, dataConvertida,))
        listaDadosRetorno = SensorService_pb2.ListaDados()
        for id, data, id_sensor, localizacao, valor in cur:
            dadoRetorno = SensorService_pb2.Dado(id=id, data=data.strftime("%d/%m/%Y, %H:%M:%S"), localizacao=localizacao, valor=valor)
            listaDadosRetorno.dados.append(dadoRetorno)
        conn.close()    
        return listaDadosRetorno

        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    SensorService_pb2_grpc.add_SensorServiceServicer_to_server(SensorServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


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


if __name__ == '__main__':
    serve()