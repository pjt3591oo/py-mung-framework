from mung.scaffold import Scaffold
from functools import wraps

class Route(Scaffold):
  def __init__(self):
    super().__init__()

  def only_slash_remove(self, path):
    if path == '/':
      return ''
    return path
  
  def get(self, path):
    def wrapper(func):
      self.add_GET(self.only_slash_remove(path), func)
      def excutor(*args, **kwargs):
        return func(*args, **kwargs)
      return excutor

    return wrapper

  def post(self, path):
    def wrapper(func):
      self.add_POST(self.only_slash_remove(path), func)

      def excutor(*args, **kwargs):
        return func(*args, **kwargs)
      return excutor

    return wrapper

  def put(self, path):
    def wrapper(func):
      self.add_PUT(self.only_slash_remove(path), func)
      def excutor(*args, **kwargs):
        return func(*args, **kwargs)
      return excutor

    return wrapper

  def delete(self, path):
    def wrapper(func):
      self.add_DELETE(self.only_slash_remove(path), func)

      def excutor(*args, **kwargs):
        return func(*args, **kwargs)
      return excutor

    return wrapper