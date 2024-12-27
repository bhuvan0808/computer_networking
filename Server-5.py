import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service.
port = 9999

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Wait for client connection.
server_socket.listen(1)

# Establish connection with client.
client_socket, client_address = server_socket.accept()

print(f"Connection from {client_address} has been established.")

# Receive and send messages
while True:
    # Receive message from client
    message = client_socket.recv(1024).decode()
    print(f"Received message: {message}")

    # Send message to client
    reply = input("Enter your message: ")
    client_socket.send(reply.encode())