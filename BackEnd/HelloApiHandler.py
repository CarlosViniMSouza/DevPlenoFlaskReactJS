from flask_restful import Resource, reqparse


class HelloApiHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message': "API WORKING"
        }

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('dataInit', type=str)
        parser.add_argument('dataEnd', type=str)

        args = parser.parse_args()

        print(args)
        # note, o post req do frontend precisa corresponder as strings aqui (por exemplo, 'type and 'message')

        di = args['dataInit']
        df = args['dataEnd']

        # atualmente apenas retornando o req direto
        data_init = di
        data_end = df

        if data_end:
            message = f"Your requisition: {data_init} \n {data_end}"
        else:
            message = "Nothing requisition"

        result = {"status": "Success", "messagem": message}

        return result
