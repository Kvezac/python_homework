import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 4321
print(host)
client_socket.connect((host, port))


server_message = client_socket.recv(1024).decode()
print(server_message)


while True:
    client_message = input("Enter your message: ")
    client_socket.send(client_message.encode())

    if not client_message:
        print("Disconnecting from the server...")
        break

    server_response = client_socket.recv(1024).decode()
    print(f"Server response:\n{server_response}")
client_socket.close()
