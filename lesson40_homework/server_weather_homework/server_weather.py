import socket
import threading
from api_weather import get_request

"""Измените задание номер 2. Добавьте получение прогноза погоды из внешнего источника
   Для этого воспользуйтесь сайтом https://openweathermap.org.
   Для начала нужно зарегистрироваться на сайте по
   ссылке https://home.openweathermap.org/users/sign_up
   и получить ключ для дальнейшей работы. На странице
   https://openweathermap.org/current есть подробная документация как работать с API. Теперь после запроса от
   клиента необходимо получать данные о погоде с этого
   источника. Полученный результат возвращать клиенту."""

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 4321

server_socket.bind((host, port))
print(f'The server is running at {host}, port {port}')

server_socket.listen(5)

welcome_message = 'Welcome! You are connected to a weather server\n' \
                  'Enter a message in the form "City": '


def handle_client(client_socket, client_address):
    print(f'Client connected: {client_address}')
    client_socket.send(welcome_message.encode())

    while True:
        client_message = client_socket.recv(1024).decode()

        if not client_message:
            print('Client disconnected: ', client_address)
            break

        query = client_message.title()
        answer = get_request(query)
        client_socket.send(answer.encode())

    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
