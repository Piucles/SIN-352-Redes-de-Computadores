import socket

server_name = "127.0.0.1"
server_port = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Digite uma frase em minúsculas: ")
client_socket.sendto(message.encode(), (server_name, server_port))

modified_message, server_address = client_socket.recvfrom(2048)
print("Resposta do Servidor:", modified_message.decode())

client_socket.close()
