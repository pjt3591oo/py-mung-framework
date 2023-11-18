from urllib import parse
import json

class Request:
  def __init__(self, http_ctx):
    self.http_ctx = http_ctx

    parsed_path = parse.urlparse(http_ctx.path)
    self.path = parsed_path.path or '/'
    self.qs = self.parse_qs(parsed_path.query)
    self.headers = self.parse_headers()
    self.body = self.parse_body()

  def parse_headers(self):
    headers = dict(self.http_ctx.headers.items())
    return headers

  def parse_body(self):
    if not self.http_ctx.headers['Content-Length'] :
      return {}
    content_length = int(self.http_ctx.headers['Content-Length'])
    body_data = self.http_ctx.rfile.read(content_length) # <--- Gets the data itself
    return json.loads(body_data)

  def parse_qs(self, query):
    qs={}

    if query == '':
      return qs

    for x in query.split('&'):
      y = x.split("=")
      if len(y) >= 1:
          qs[y[0]] = y[1] or ''

    return qs