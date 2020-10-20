import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  ## Create Doorway
mysock.connect(('data.pr4e.org', 80))  ## Connect to server
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()   ## Prepare for sending
mysock.send(cmd)  ## Send the request - crucial and this is used to hack the servers

## using the while loop to decode and interpret the recieved result and also to
## to break if no data recieved

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

## Closet the socket
mysock.close()
