import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the IP address of the server
server_address = '10.106.2.215'

# Reserve a port for your service.
port = 9999

# Connect to the server.
client_socket.connect((server_address, port))

# Send and receive messages
while True:
    # Send message to server
    message = input("Enter your message: ")
    client_socket.send(message.encode())

    # Receive message from server
    reply = client_socket.recv(1024).decode()
    print(f"Received message: {reply}")