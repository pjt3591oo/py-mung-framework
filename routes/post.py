from mung.route import Route

post_route = Route()
post = []

@post_route.get('/')
def read_all_post(req, res):
  return res.status(200).json({
    'range': f'{req.qs.get("start", 0)} ~ {req.qs.get("end", 0)}',
    'data': post[int(req.qs.get("start", 0)): int(req.qs.get("end", 0))]
  })

@post_route.post('/')
def register_post(req, res):
  post_info = req.body
  post.append(post_info)
  return res.status(200).json({
    'data': post_info
  })