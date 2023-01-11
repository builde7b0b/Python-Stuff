import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 4242))
s.send('Hello, world')   # This returns how many bytes were sent
data = s.recv(1024)
s.close()
print 'Received', 'data'

"""Builds a client that connects to a remote(or local) host and sends 'Hello, world'.
To test, we need a server.
Simulate server by binding netcat listener to port 4242
# nc -l -p 4242
"""
