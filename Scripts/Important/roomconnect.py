import threading


import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 14242

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_HOST, SERVER_PORT))

while True:
    message = input()
    if message == "":
        break
    client_socket.sendall(message.encode())
