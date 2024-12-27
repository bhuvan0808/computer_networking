import socket

# define the server's IP address and port
HOST = '10.106.2.215'  # replace with the server's IP address
PORT = 12345  # replace with the same port used by the server

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect((HOST, PORT))
print(f"Connected to {HOST}:{PORT}")

# read the file to send
with open("C:\Users\manis\OneDrive\Desktop\VS_CODE\python\LAB6\File_to_send.txt", "rb") as f:
    file_data = f.read()

# send the file to the server
client_socket.sendall(file_data)

# close the connection and the socket
client_socket.close()