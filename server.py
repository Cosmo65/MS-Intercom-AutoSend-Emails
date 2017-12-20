from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_Intercom(BaseHTTPRequestHandler):
	pass

def run_server():
	print("Starting server...")

	server_address = ('127.0.0.1', 8080)
	httpd = HTTPServer(server_address, HTTPServer_Intercom)
	print("Running server...")
	httpd.serve_forever()
