import SocketServer, SimpleHTTPServer, multiprocessing


def server_start(port):
	'''Starts Python's SimpleHTTPServer on specified port'''
	httpPort = int(port)
	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = SocketServer.TCPServer(("",httpPort), Handler, bind_and_activate=False)
	httpd.allow_reuse_address = True
	server_process = multiprocessing.Process(target=httpd.serve_forever)
	server_process.daemon = False
	try:
		httpd.server_bind()
		httpd.server_activate()
	except:
		httpd.server_close()
	# Create process
	server_process.start()

	serverPid=server_process.pid
  
  	return serverPid

def server_kill():
	try:
		# print('Trying to stop server process %s' % str(serverPid))
		os.kill(int(serverPid),9)
	except Exception as e:
		print(e)
