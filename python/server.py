# server.py


import socket 

host =  ''
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print 'Waiting for connections...'
clientsock, clientaddr = s.accept()

while 1:
	rcvmsg = clientsock.recv(1024)
	print 'You received a message > %s' % (rcvmsg)
	if rcvmsg == '':
		break
clientsock.close()
