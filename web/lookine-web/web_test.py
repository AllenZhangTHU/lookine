#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import time, threading

PORT_NUMBER = 8081

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/":
			self.path="/index.html"

		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)
def runserver(portNum):
	try:
		#Create a web server and define the handler to manage the
		#incoming request
		server = HTTPServer(('', portNum), myHandler)
		print 'Started httpserver on port ' , PORT_NUMBER
		#Wait forever for incoming htto requests
		server.serve_forever()
	except KeyboardInterrupt:
		print '^C received, shutting down the web server'
		server.socket.close()


t = threading.Thread(target=runserver, args=(PORT_NUMBER,))
t.start()
print "222222"
t.join()
	