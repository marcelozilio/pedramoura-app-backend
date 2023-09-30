from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class RotasByStatus(Resource):
    def get(self, status):
        response = make_response(jsonify({
            'id': 1,
            'quantidade': 10,
            'dataEntrega': '20/09/2023',
            'kms': 102,
            'status': 'PRONTA_PARA_ENTREGA'
        }))
        response.headers['Content-Type'] = 'application/json'
        return response


class PedidoById(Resource):
    def put(self, id):
        response = make_response(make_response(jsonify({
            'status': 'ok',
            'msg': 'pedido atualizado'
        })))
        response.headers['Content-Type'] = 'application/json'
        return response


    def get(self, id):
        response = make_response(jsonify(
        {
            'id': 123,
            'idRota': 1,
            'nomeCliente': 'Jaqueline',
	        'endereco': 'Av. Inconfidência 1002, Canoas',
	        'observacoes': 'Portão Amarelo',
	        'telefone': '(51) 99257-8631',
	        'itensPedido': ['1 kg - Carne moída', '5 kg - Picanha'],
            'status': 'EM_ROTA',
            'observacoesEntrega': 'Entregar para o vizinho'
        }
        ))
        response.headers['Content-Type'] = 'application/json'
        return response

class PedidoByIdRota(Resource):
    def get(self, idRota):
        response = make_response(jsonify(
        {
            'id': 123,
            'idRota': 1,
            'nomeCliente': 'Jaqueline',
	        'endereco': 'Av. Inconfidência 1002, Canoas',
	        'observacoes': 'Portão Amarelo',
	        'telefone': '(51) 99257-8631',
	        'itensPedido': ['1 kg - Carne moída', '5 kg - Picanha']
        },
        {
            'id': 124,
            'idRota': 1,
            'nomeCliente': 'Rodrigo',
	        'endereco': 'R. Marechal 782, Canoas',
	        'observacoes': 'Em frente ao mercado do Rogério',
	        'telefone': '(51) 99278-8481',
	        'itensPedido':['3 kg - Coxão de dentro', 'Carvão 5kg']
        }
        ))
        response.headers['Content-Type'] = 'application/json'
        return response


api.add_resource(RotasByStatus, '/rotas/<status>')
api.add_resource(PedidoById, '/pedidos/<id>')
api.add_resource(PedidoByIdRota, '/rotas/<idRota>/pedidos/')


if __name__ == '__main__':
    app.run()
