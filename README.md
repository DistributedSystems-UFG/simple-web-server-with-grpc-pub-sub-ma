# simple-web-server-with-grpc-pub-sub-ma

Atividade Pub-Sub
Disciplina: Software para Sistemas Ubíquos
Alunos: 
- Ariel Marte (201900264)
- Marco Feitosa (201905542)

# Contexto
Simulando notificaçãoo de equipamentos que monitoram a cada 30 segundos as condições
 de temperatura salas de servidores, utilizando kafka, gRPC e Gooogle Cloud.
 
# Demonstração

[Link para video no Youtube](https://youtu.be/1Gf43pl_zEU "Link para video no Youtube")


## Configuração

Passo a passo:

1) Instale o PIP.

`sudo apt install python3-pip`

2) Atualize o PIP

`python3 -m pip install --upgrade pip`

3) Instale o tempo de execução do gRPC

`python3 -m pip install grpcio`

4) Instale as ferramentas gRPC

`python3 -m pip install grpcio-tools`

5) Clone este repositório

6) Compile a especificação da interface (arquivo .proto de buffers de protocolo)

`cd python`

`python3 -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/SensorService.proto `

7) Instale o Banco de Dados

`pip install mariadb`
