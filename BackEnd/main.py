# Full Example to Docs
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from setup_data import dados

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados'

info = dados()


# route of welcome
@app.route("/")
def welcome():
    return "<h2>Welcome<h2>"


@app.route("/somatorio")
def somatorio():
    return f"<p>A soma dos valores eh = ${info}</p>"


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message=f"Todo {todo_id} doesn't exist")


parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]


# TodoList - shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


# Actually setup the Api resource routing here
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
