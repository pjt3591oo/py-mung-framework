class Scaffold:

  def __init__(self):
    self.MAP_METHOD_POST = []
    self.MAP_METHOD_GET = []
    self.MAP_METHOD_DELETE = []
    self.MAP_METHOD_PUT = []

  def add_GET(self, path, func):
    self.MAP_METHOD_GET.append({
      'path': path,
      'func': func,
    })

  def add_POST(self, path, func):
    self.MAP_METHOD_POST.append({
      'path': path,
      'func': func,
    })

  def add_PUT(self, path, func):
    self.MAP_METHOD_PUT.append({
      'path': path,
      'func': func,
    })

  def add_DELETE(self, path, func):
    self.MAP_METHOD_DELETE.append({
      'path': path,
      'func': func,
    })