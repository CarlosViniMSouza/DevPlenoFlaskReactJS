from flask import Flask, request
from flask_restful import Resource, Api
from requests import put, get

app = Flask(__name__)
api = Api(app)
URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados'
todos = {}


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

"""
1. O principal bloco de construção fornecido pelo Flask-RESTful são os recursos(Resource). Os recursos são criados com base nas visualizações conectáveis do Flask, oferecendo acesso fácil a vários métodos HTTP apenas definindo métodos em seu recurso.

2. Flask-RESTful entende vários tipos de valores de retorno de métodos de exibição. Semelhante ao Flask, você pode retornar qualquer iterável e ele será convertido em uma resposta, incluindo objetos de resposta brutos do Flask. O Flask-RESTful também oferece suporte à configuração do código de resposta e dos cabeçalhos de resposta usando vários valores de retorno.
"""
