from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# criando um app flask
app = Flask(__name__)
# criando uma API objeto
api = Api(app)

# tornando uma classe para um recurso especifico os metodos get, post correspondem a solicitacoes get e post eles sao mapeados automaticamente por flask_restful. Outros metodos incluem put, delete, etc.


class Hello(Resource):

    # corresponde a solicitacao GET.
    # esta função e chamada sempre que ha um pedido GET para este recurso
    def get(self):
        return jsonify({'message': 'hello world'})

    # Corresponde a POST
    def post(self):
        data = request.get_json()
        return jsonify({'data': data}), 201


# outro recurso para calcular o quadrado de um número
class Square(Resource):

    def get(self, num):
        return jsonify({'square': num})


# adicionando os recursos definidos junto com seus URLs correspondentes
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')


# executar
if __name__ == '__main__':
    app.run(debug=True)
