# client.py


import socket

host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while 1: 
	print 'Type message you want to send to %s ...' % (host)
	msg = raw_input()
	if msg == '':
		s.close()
		break
	s.sendall(msg)

