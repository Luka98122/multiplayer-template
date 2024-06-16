import client
import random
client_socket,server_thread,clients = client.setup()
a = random.randint(10,1000)
client_socket.sendall(f"<set_name>Tester{a}".encode())

prefixes = [["/ac ","<ac>"],["/dm ","<dm>"],["/name ","<set_name>"]]


while True:
    message = input()
    if message=="":
        exit()
        break
    elif message == ".l":
        for cli in clients:
            cli.pr()
    else:
        for pre in prefixes:
            message = message.replace(pre[0],pre[1])
        client_socket.sendall(message.encode())