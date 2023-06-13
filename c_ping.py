import time
from socket import *
#Objeto usado para enviar e receber dados AF_INET -> Define o tipo de endereçamento, sendo IPV4, SOCK_DGRAM -> Define o tipo de socket a ser criado, sendo UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

clientAddress = ('127.0.0.1', 50000)

serverSocket.settimeout(1)

tempos = []
quantidadePacotesPerdidos = 0

contador = 0
while contador < 10:
    try:
        message = "Hello world %s" %contador
        tempoInicial = time.time()
        serverSocket.sendto(message.encode(), clientAddress)

        response, addr = serverSocket.recvfrom(1024)
        tempoFinal = time.time()
        tempo = (tempoFinal - tempoInicial) * 1000
        tempos.append(tempo)
        
        print(response, addr)
        print(f"Tempo do pacote {tempo:.2f}")
        contador += 1
    except:
        quantidadePacotesPerdidos += 1
        print("Timeout Ocorreu")

print("Fechando conexao")
serverSocket.close()

tempoMinimo = min(tempos)
tempoMaximo = max(tempos)
tempoMedio = sum(tempos) / len(tempos)
porcentagemPacotesPerdidos = (quantidadePacotesPerdidos * 10)

print(f"Tempo minimo: {tempoMinimo:.2f} s")
print(f"Tempo maximo: {tempoMaximo:.2f} s")
print(f"Tempo medio: {tempoMedio:.2f} s")
print(f"Porcentagem dos pacotes perdidos: {porcentagemPacotesPerdidos:.2f}%")
