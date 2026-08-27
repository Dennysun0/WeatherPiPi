from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from storage import guardar_temperatura



class Servidor(BaseHTTPRequestHandler):
	
	def do_GET(self):
		
		if self.path == "/":
			
			with open("web/index.html", "rb") as archivo:
				contenido = archivo.read()
		

		
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()

			self.wfile.write(contenido)

		elif self.path == "/scripts.js":
			with open("web/scripts.js", "rb") as archivo:
				contenido = archivo.read()

			self.send_response(200)
			self.send_header("Content-type", "application/javascript")
			self.end_headers()

			self.wfile.write(contenido)

		elif self.path == "/style.css":
			with open("web/style.css", "rb") as archivo:
				contenido = archivo.read()
			self.send_response(200)
			self.send_header("Content-type", "text/css")
			self.end_headers()

			self.wfile.write(contenido)

		elif self.path == "/images/foto_web.jpg":
			with open("web/images/foto_web.jpg", "rb") as archivo:
				contenido = archivo.read()
			self.send_response(200)
			self.send_header("Content-type", "image/jpeg")
			self.end_headers()

			self.wfile.write(contenido)

		elif self.path == "/temperaturas":

			with open("datos/temperaturas.json", "rb") as archivo:
				contenido = archivo.read()

			self.send_response(200)
			self.send_header("Content-type", "application/json")
			self.end_headers()
			self.wfile.write(contenido)


	def do_POST(self):
		longitud = int(self.headers["Content-Length"])

		datos = self.rfile.read(longitud)
		datos = datos.decode("utf-8")
		datos = json.loads(datos)

		print(datos)

		guardar_temperatura(
			datos["dia"],
			datos["minima"],
			datos["maxima"]
		)

		self.send_response(200)
		self.end_headers()

		self.wfile.write(b"Datos recibidos correctamente")

servidor = HTTPServer(("0.0.0.0", 8000), Servidor)

print("Servidor iniciado en el puerto 8000")

servidor.serve_forever()
