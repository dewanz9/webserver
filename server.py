import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("", 80)

print "starting server on port:", server_address

server.bind(server_address)

server.listen(5)

running = True
while running:
	connection, client_address = server.accept()
	print "connection from",connection.getpeername()
	temp = ""
	file_path=""
	webby=""
	reply=""
	data=""

	data = connection.recv(4096)
	print data

	temp = data.split("\n")
	file_path = temp[0].split()[1]


	if file_path[-4:] == ".png":
		image = open(file_path[1:],"r")
		data2 = image.read(1024)
		print "----------------"
		while (data2):
			print "sending...."
			connection.send(data2)
			data2 = image.read(1024)
		


	else:
		try:
			if file_path[1:] == "":
				file_path = "/index.html"
			webby = open(file_path[1:])
			reply = ""
			for line in webby:
				reply = reply + line
	        print "response sent"
	        connection.send(reply)
		except:
			reply = "<h1>page not found</h1>"
			connection.send(reply)





	connection.shutdown(socket.SHUT_RD | socket.SHUT_WR)
	connection.close()
	print "connection closed"






server.close()

