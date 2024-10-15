#import socket module
from socket import *
import sys  # In order to terminate the program

# Create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
serverSocket.bind(('', 6789))  # Bind the socket to server address and port 6789
serverSocket.listen(1)  # Listen for incoming connections (max. 1 queued connection)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in start
    connectionSocket, addr = serverSocket.accept()  
    # Fill in end
    try:
        # Fill in start
        message = connectionSocket.recv(1024).decode()
        # Fill in end
        filename = message.split()[1] 
        f = open(filename[1:])       
        # Fill in start
        outputdata = f.read() 
        # Fill in end 
       
        # Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())  
        # Fill in end
         
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())  
        connectionSocket.close()

    except IOError:
       
        # Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Fill in end
        
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  
