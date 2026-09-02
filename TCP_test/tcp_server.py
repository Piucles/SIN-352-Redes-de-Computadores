import socket

HOST = "127.0.0.1"  # Interface de loopback
PORT = 12000        # Porta de escuta

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor TCP aguardando conexão...")
    conn, addr = s.accept()
    with conn:
        print(f"Conectado por: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)