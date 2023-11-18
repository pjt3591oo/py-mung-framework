from mung.route import Route

user_route = Route()
users = []

@user_route.get('/')
def read_all_user(req, res):
  return res.status(200).json({
    'data': users
  })

@user_route.post('/')
def register_user(req, res):
  user_info = req.body
  users.append(user_info)
  return res.status(200).json({
    'data': user_info
  })