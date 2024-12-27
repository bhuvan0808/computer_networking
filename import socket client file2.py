import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the IP address and port of the server
host = '10.106.10.229' # Replace with the IP address of the server
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Prompt the user for their student roll number
roll_number = input('Enter your student roll number:  ')

# Send the roll number to the server
client_socket.send(roll_number.encode('utf-8'))

# Receive the device identity from the server
device_identity = client_socket.recv(1024).decode('utf-8')

# Print the device identity
print('The device identity for roll number %s is %s' % (roll_number, device_identity))

# Send an acknowledgement to the server
acknowledgement = 'Received device identity for roll number %s' % roll_number
client_socket.send(acknowledgement.encode('utf-8'))

# Close the connection
client_socket.close()
