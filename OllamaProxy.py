import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import requests
import sys

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Clase que permite manejar múltiples solicitudes en hilos separados."""
    pass

class ReverseProxy(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request("GET")

    def do_POST(self):
        self.handle_request("POST")

    def do_PUT(self):
        self.handle_request("PUT")

    def do_DELETE(self):
        self.handle_request("DELETE")

    def do_HEAD(self):
        self.handle_request("HEAD")

    def handle_request(self, method):
        try:
            # Ignorar solicitudes a favicon.ico
            if self.path == "/favicon.ico":
                self.send_response(404)
                self.end_headers()
                return

            # Reconstruir la URL de destino
            target_url = f"{self.server.target_url}{self.path}"
            print(f"Proxying {method} request to {target_url}")

            # Reenviar encabezados y establecer el encabezado Host correcto
            headers = {key: value for key, value in self.headers.items()}
            headers["Host"] = self.server.target_host

            # Enviar la solicitud a la URL de destino
            if method in ["POST", "PUT"]:
                content_length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_length)
                response = requests.request(method, target_url, headers=headers, data=body, stream=True)
            else:
                response = requests.request(method, target_url, headers=headers, stream=True)

            # Enviar la respuesta de vuelta al cliente
            self.send_response(response.status_code)
            for header_key, header_value in response.headers.items():
                if header_key.lower() == "transfer-encoding" and header_value.lower() == "chunked":
                    continue
                self.send_header(header_key, header_value)
            self.end_headers()

            # Transmitir el contenido de la respuesta al cliente
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    self.wfile.write(chunk)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())

def show_credits():
    print("\n==============================")
    print("  Reverse Proxy creado por HirCoir")
    print("  Sitio web: hircoir.eu.org")
    print("  GitHub: github.com/HirCoir")
    print("\n  Este script crea un túnel ngrok para redirigir solicitudes a la API de Ollama.")
    print("==============================\n")

def sanitize_url(url):
    return url.rstrip('/')

def run_proxy(server_class=ThreadedHTTPServer, handler_class=ReverseProxy, port=11434, target_url=None):
    show_credits()

    if not target_url:
        target_url = input("Introduce la URL de ngrok (ejemplo: https://ejemplo.ngrok.io): ")
    target_url = sanitize_url(target_url)
    target_host = target_url.split("//")[-1]

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.target_url = target_url
    httpd.target_host = target_host
    print(f"Reverse proxy running on port {port}, redirecting to {target_url}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nProxy detenido. Presiona Ctrl+C nuevamente para mostrar el código fuente.")
        try:
            input("Presiona Enter para salir...")
        except KeyboardInterrupt:
            print("\nMostrando el código fuente:\n")
            with open(sys.argv[0], 'r') as file:
                print(file.read())
        finally:
            httpd.server_close()

def main():
    parser = argparse.ArgumentParser(description="Inicia un proxy inverso para la API de Ollama usando ngrok.")
    parser.add_argument("--url", type=str, help="URL de ngrok a redirigir (ejemplo: https://ejemplo.ngrok.io)")
    parser.add_argument("--port", type=int, default=11434, help="Puerto local para el proxy (por defecto: 11434)")
    args = parser.parse_args()

    if args.url:
        print("Iniciando con los argumentos proporcionados...")
        run_proxy(port=args.port, target_url=sanitize_url(args.url))
    else:
        print("Iniciando en modo interactivo...")
        run_proxy(port=args.port)

if __name__ == "__main__":
    main()
