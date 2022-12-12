import grpc
from concurrent import futures
import SensorService_pb2
import SensorService_pb2_grpc

channel = grpc.insecure_channel('34.72.20.20'+':'+'50051')

def consultarPorLocalizacao(local: str):
    stub = SensorService_pb2_grpc.SensorServiceStub(channel)

    loc = SensorService_pb2.Localizacao(localizacao=local)
    response = stub.ConsultarListaPorLocalizacao(loc)
    print ('Dados: ' + str(response.dados))

def consultarPorData(data: str):
    stub = SensorService_pb2_grpc.SensorServiceStub(channel)

    dataStub = SensorService_pb2.Data(data=data)
    response = stub.ConsultarListaPorData(dataStub)
    print ('Dados: ' + str(response.dados))   

def consultarPorLocalizacaoELocalizacao(local : str, data : str):
    stub = SensorService_pb2_grpc.SensorServiceStub(channel)
    loc = SensorService_pb2.Localizacao(localizacao=local)
    dataStub = SensorService_pb2.Data(data=data)
    locData = SensorService_pb2.LocalData(local=loc, data=dataStub)
    response = stub.ConsultarListaPorDataELocalizacao(locData)
    print ('Dados: ' + str(response.dados))


if __name__ == '__main__':
    print('Selecione a opcao desejada:')
    print('1 - Listar por localizacao\n')
    print('2 - Listar por data\n')
    print('3 - Listar por localizacao e data\n')
    opcao = int(input('Opcao: '))
    
    localizacao = ''
    data = ''
    if(opcao == 1 or opcao == 3):
        localizacao = str(input('Localização: '))
    if(opcao == 2 or opcao == 3):
        data = str(input('Data: '))
    
    if(opcao == 1):
        consultarPorLocalizacao(localizacao)
        exit
    
    if(opcao == 2):
        consultarPorData(data)
        exit
        
    if(opcao == 3):
        consultarPorLocalizacaoELocalizacao(localizacao, data)
        exit