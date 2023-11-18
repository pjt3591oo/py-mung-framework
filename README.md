# Mung Web Framework

* post route

```python
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
```

* user route

```python 
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
```

* Mung Application

```python
from mung.mung import Mung

from routes.user import user_route
from routes.post import post_route

app = Mung('0.0.0.0', 3000)

app.use('/post', post_route)
app.use('/user', user_route)

app.run()
```

* run 

```bash
$ python server.py
```

### API 테스트

*  유저 생성

```bash
$ curl --location 'localhost:3000/user' \
--header 'Content-Type: application/json' \
--data '{
    "name": "멍개111",
    "age": 31
}'

# 응답결과
{"data": {"name": "\uba4d\uac1c111", "age": 31}}
```

```bash
$ curl --location 'localhost:3000/user' \
--header 'Content-Type: application/json' \
--data '{
    "name": "멍개000",
    "age": 30
}'

# 응답결과
{"data": {"name": "\uba4d\uac1c000", "age": 30}}
```

* 유저목록 조회

```bash
$ curl --location 'localhost:3000/user'

# 응답결과
{"data": [{"name": "\uba4d\uac1c111", "age": 31}, {"name": "\uba4d\uac1c000", "age": 30}]}
```

* 게시글 생성

```bash
$ curl --location 'localhost:3000/post' \
--header 'Content-Type: application/json' \
--data '{
    "title": "title0",
    "body": "body0"
}'

# 응답결과
{"data": {"title": "title0", "body": "body0"}}
```

* 게시글 조회

```bash
$ curl --location 'localhost:3000/post?start=0&end=2'

# 응답결과
{"range": "0 ~ 2", "data": [{"title": "title0", "body": "body0"}]}
```

* 404 테스트

```bash
$ curl --location 'localhost:3000/' --raw -i  

# 응답결과
HTTP/1.0 404 Not Found
Server: BaseHTTP/0.6 Python/3.10.5
Date: Sat, 18 Nov 2023 08:45:06 GMT
Content-type: application/json

{}
```