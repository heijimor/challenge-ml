from http.server import HTTPServer
from routing.base_request_handler import BaseRequestHandler

def run_server():
  port = 8000
  server_address = ('', port)
  httpd = HTTPServer(server_address, BaseRequestHandler)
  print(f'Starting server... {port}')
  httpd.serve_forever()


if __name__ == '__main__':
  try: 
    run_server()
  except:
    print('error')