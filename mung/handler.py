from http.server import BaseHTTPRequestHandler
from mung.req import Request
from mung.res import Response

def handler_factory(routes):
  class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
      route_root_path, route = self.is_root_path()
      self.handle_by_route(route_root_path, route.MAP_METHOD_GET) if route_root_path else self.handle_404()

    def do_POST(self):
      route_root_path, route = self.is_root_path()
      self.handle_by_route(route_root_path, route.MAP_METHOD_POST) if route_root_path else self.handle_404()
    
    def do_PUT(self):
      route_root_path, route = self.is_root_path()
      self.handle_by_route(route_root_path, route.MAP_METHOD_PUT) if route_root_path else self.handle_404()

    def do_DELETE(self):
      route_root_path, route = self.is_root_path()
      self.handle_by_route(route_root_path, route.MAP_METHOD_DELETE) if route_root_path else self.handle_404()

    def is_root_path(self):
      for route_root_path, route in routes.items():
        if self.path.find(route_root_path) == 0:
          return route_root_path, route
      
      return None, None
      
    def handle_by_route(self, route_root_path, route_map):
      if route_map is None or route_root_path is None:
        self.handle_404()
        return

      for item in route_map:
        route_path = item['path']

        if self.path.split('?')[0] == route_root_path + route_path:
          res = item['func'](Request(self), Response(self))
          res.emit_response()
          return
      
      self.handle_404()

    def handle_404(self):
      res = Response(self)
      res.status(404)
      res.emit_response()

  return Handler