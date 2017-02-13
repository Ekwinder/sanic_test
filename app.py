from sanic import Sanic
from test import handler1, handler2, person_handler2

app = Sanic(__name__)

app.add_route(handler1, '/')
app.add_route(handler1, '/test')
app.add_route(handler2, '/folder/<name>')
app.add_route(person_handler2, '/person/<name:[A-z]>', methods=['GET'])
app.run(host="0.0.0.0", port=8000, debug=True)
