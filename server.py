from mung.mung import Mung

from routes.user import user_route
from routes.post import post_route

app = Mung('0.0.0.0', 3000)

app.use('/post', post_route)
app.use('/user', user_route)

app.run()