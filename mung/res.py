import json 

class Response:
  def __init__(self, http_ctx):
    self.http_ctx = http_ctx

    self.response_status = 200
    self.headers = [
      ['Content-type', 'application/json']
    ]
    self.data = {}
    
  def header(self, header):
    self.headers.append(header)
    return self

  def status(self, status):
    self.response_status = status
    return self

  def json(self, data):
    self.data = data
    return self
  
  def set_headers(self, headers):
    for header in headers:
      self.http_ctx.send_header(header[0], header[1])

  def emit_response(self):
    self.http_ctx.send_response(self.response_status)
    
    self.set_headers(self.headers)

    self.http_ctx.end_headers()

    self.http_ctx.wfile.write(json.dumps(self.data).encode('utf-8'))