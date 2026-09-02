import socket

server_port = 12000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", server_port))

print("Servidor UDP pronto para receber...")

while True:
    message, client_address = server_socket.recvfrom(2048)
    print(f"Recebido de {client_address}: {message.decode()}")
    modified_message = message.upper()
    server_socket.sendto(modified_message, client_address)
    