## Programei o desenvolvimento de um cliente TCP usando SOCKET e SYS no PYTHON
import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("socket criado com sucesso")

    HostAlvo = input("Digite o host ou Ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com Sucesso no Host: " + HostAlvo + "e na porta: " + PortaAlvo)
        s.shutdown(1)
    except socket.error as e:
        print("Não foi possivel se conectar no Host: " + HostAlvo + "- porta: " + PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()

