import socket

# define host and port to listen on
HOST = '10.106.2.215'  # listens on all available network interfaces
PORT = 12345  # choose any free port you like

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the specified host and port
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen(1)
print(f"Listening on {HOST}:{PORT}")

# wait for a client to connect
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# receive a file from the client
file_data = client_socket.recv(1024)

# write the file to disk
with open("received_file", "wb") as f:
    f.write(file_data)

# close the connection and the socket
client_socket.close()
server_socket.close()