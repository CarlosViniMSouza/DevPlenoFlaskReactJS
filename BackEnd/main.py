# Full Example to Docs
from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from setup_data import dados
from HelloApiHandler import HelloApiHandler


app = Flask(__name__, static_url_path='',
            static_folder='../FrontEnd/desafiodevpleno')

api = Api(app)
info = dados()

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados'
CORS(app)


@app.route("/", defaults={'path': ''})
def servidor(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/somatorio")
def somatorio():
    return f"<p>A soma dos valores eh = ${info}</p>"


api.add_resource(HelloApiHandler, '/flask/hello')


if __name__ == '__main__':
    app.run(debug=True)
