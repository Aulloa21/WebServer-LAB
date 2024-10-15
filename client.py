from socket import *
import sys  # For command line arguments and error handling

# Ensure the correct number of command line arguments are provided
if len(sys.argv) != 4:
    print("Usage: python client.py <server_host> <server_port> <filename>")
    sys.exit()

# Extract command line arguments
server_host = sys.argv[1]  # Server IP or hostname
server_port = int(sys.argv[2])  # Server port number
filename = sys.argv[3]  # File requested from the server

# Create a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Establish connection to the server
try:
    clientSocket.connect((server_host, server_port))
except Exception as e:
    print(f"Failed to connect to the server: {e}")
    sys.exit()

# Send an HTTP GET request to the server
request_line = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"
clientSocket.send(request_line.encode())

# Receive the response from the server
response = clientSocket.recv(4096)  # Adjust buffer size as needed
print("Server response:\n")
print(response.decode())

# Close the connection
clientSocket.close()
