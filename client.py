import json
import socket
import threading

# Open the JSON file and read its contents
with open('info.json', 'r') as f:
    data = f.read()
# read the file content as a dic
info = json.loads(data)

# the conection variables
server_host = info['host']
server_port = info['port']
name = info['name']

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect((server_host, server_port))
# once connected, send the name
client_socket.send(f'~{name}'.encode())

def receive_messages():
    """Receive messages from the server."""
    while True:
        # Receive a message from the server
        message = client_socket.recv(1024).decode()
        if not message:
            break

        # Print the message
        print(message)

# Start a new thread to receive messages
thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    # Send a message to the server
    message = input('')
    # if the user wants to leave
    if message == ';':
        message = f'\n-> {name} se desconectó'
        client_socket.send(message.encode())
        break
    else: 
        message = f'[{name}]: {message}'
        client_socket.send(message.encode())

# Close the connection
client_socket.close()

