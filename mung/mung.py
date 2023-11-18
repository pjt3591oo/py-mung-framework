from http.server import HTTPServer

from mung.logging import application_start_print, route_resolve_print
from mung.handler import handler_factory

class Mung:
  routes = {}

  def __init__(self, host, port):
    self.host = host
    self.port = int(port)
  
  def use(self, path, route):
    self.routes[path] = route

  def run(self):
    self.loging()
    handler = handler_factory(self.routes)
    httpd = HTTPServer((self.host, self.port), handler)
    httpd.serve_forever()

  def loging(self):
    application_start_print()

    for route_root_path, route in self.routes.items():
      for item in route.MAP_METHOD_GET:
        detail_path = item['path']
        route_resolve_print('GET', route_root_path + detail_path)

      for item in route.MAP_METHOD_POST:
        detail_path = item['path']
        route_resolve_print('POST', route_root_path + detail_path)

      for item in route.MAP_METHOD_PUT:
        detail_path = item['path']
        route_resolve_print('PUT', route_root_path + detail_path)

      for item in route.MAP_METHOD_DELETE:
        detail_path = item['path']
        route_resolve_print('DELETE', route_root_path + detail_path)

