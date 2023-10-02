from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedramoura.db'  # Nome do arquivo do banco de dados SQLite
db = SQLAlchemy(app)

# Definição do modelo para a tabela "Rota"
class Rota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    dataEntrega = db.Column(db.String(10), nullable=False)
    kms = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(80), nullable=False)

    def __init__(self, quantidade, dataEntrega, kms, status):
        self.quantidade = quantidade
        self.dataEntrega = dataEntrega
        self.kms = kms
        self.status = status

# Definição do modelo para a tabela "Pedido"
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idRota = db.Column(db.Integer, nullable=False)
    nomeCliente = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    observacoes = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    itensPedido = db.Column(db.Text, nullable=False)
    statusEntrega = db.Column(db.String(80), nullable=False)
    observacoesEntrega = db.Column(db.String(200), nullable=False)

    def __init__(self, idRota, nomeCliente, endereco, observacoes, telefone, itensPedido, statusEntrega, observacoesEntrega):
        self.idRota = idRota
        self.nomeCliente = nomeCliente
        self.endereco = endereco
        self.observacoes = observacoes
        self.telefone = telefone
        self.itensPedido = itensPedido
        self.statusEntrega = statusEntrega
        self.observacoesEntrega = observacoesEntrega

# Endpoint para criar uma nova rota
@app.route('/rotas', methods=['POST'])
def create_rota():
    data = request.get_json()
    new_rota = Rota(quantidade=data['quantidade'], dataEntrega=data['dataEntrega'], kms=data['kms'], status=data['status'])
    with app.app_context():
        db.session.add(new_rota)
        db.session.commit()
    return jsonify({'message': 'Rota criada com sucesso!'})

# Endpoint para listar todas as rotas
@app.route('/rotas', methods=['GET'])
def get_rota():
    with app.app_context():
        status_to_search = request.args.get('status')
        rotas = Rota.query.filter_by(status=status_to_search) if status_to_search else Rota.query.all()
        rota_list = []
        for rota in rotas:
            rota_list.append({'id': rota.id, 'quantidade': rota.quantidade, 'dataEntrega': rota.dataEntrega, 'kms': rota.kms, 'status': rota.status})
        return jsonify({'rotas': rota_list})

# Endpoint para buscar uma Rota pelo ID
@app.route('/rotas/<int:rota_id>', methods=['GET'])
def get_rota_by_id(idRota):
    with app.app_context():
        rota = Rota.query.get(idRota)
        if rota:
            return jsonify({'id': rota.id, 'quantidade': rota.quantidade, 'dataEntrega': rota.dataEntrega, 'kms': rota.kms, 'status': rota.status})
        else:
            return jsonify({'message': 'Rota não encontrada'}), 404

# Endpoint para atualizar uma rota pelo ID
@app.route('/rotas/<int:idRota>', methods=['PUT'])
def update_rota(idRota):
    rota = Rota.query.get(idRota)
    if not rota:
        return jsonify({'message': 'Rota não encontrada'}), 404
    data = request.get_json()
    rota.quantidade = data['quantidade']
    rota.dataEntrega = data['dataEntrega']
    rota.kms = data['kms']
    rota.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Rota atualizada com sucesso!'})

# Endpoint para excluir uma rota pelo ID
@app.route('/rotas/<int:idRota>', methods=['DELETE'])
def delete_rota(idRota):
    rota = Rota.query.get(idRota)
    if not rota:
        return jsonify({'message': 'Rota não encontrada'}), 404
    db.session.delete(rota)
    db.session.commit()
    return jsonify({'message': 'Rota excluída com sucesso!'})

# Endpoint para criar um novo pedido
@app.route('/pedidos', methods=['POST'])
def create_pedido():
    data = request.get_json()
    new_pedido = Pedido(idRota=data['idRota'], nomeCliente=data['nomeCliente'], endereco=data['endereco'], observacoes=data['observacoes'], telefone=data['telefone'], itensPedido=json.dumps(data['itensPedido']), statusEntrega=data['statusEntrega'], observacoesEntrega=data['observacoesEntrega'])
    with app.app_context():
        db.session.add(new_pedido)
        db.session.commit()
    return jsonify({'message': 'Pedido criado com sucesso!'})

# Endpoint para listar todas os pedidos
@app.route('/pedidos', methods=['GET'])
def get_pedido():
    with app.app_context():
        rota_to_search = request.args.get('idRota')
        pedidos = Pedido.query.filter_by(idRota=rota_to_search) if rota_to_search else Pedido.query.all()
        pedido_list = []
        for pedido in pedidos:
            pedido_list.append({'id': pedido.id, 'idRota': pedido.idRota, 'nomeCliente': pedido.nomeCliente, 'endereco': pedido.endereco, 'observacoes': pedido.observacoes, 'telefone': pedido.telefone, 'itensPedido': json.loads(pedido.itensPedido), 'statusEntrega': pedido.statusEntrega, 'observacoesEntrega': pedido.observacoesEntrega})
        return jsonify({'rotas': pedido_list})

# Endpoint para buscar um Pedido pelo ID
@app.route('/pedidos/<int:idPedido>', methods=['GET'])
def get_pedido_by_id(idPedido):
    with app.app_context():
        pedido = Pedido.query.get(idPedido)
        if pedido:
            return jsonify({'id': pedido.id, 'idRota': pedido.idRota, 'nomeCliente': pedido.nomeCliente, 'endereco': pedido.endereco, 'observacoes': pedido.observacoes, 'telefone': pedido.telefone, 'itensPedido': json.loads(pedido.itensPedido), 'statusEntrega': pedido.statusEntrega, 'observacoesEntrega': pedido.observacoesEntrega})
        else:
            return jsonify({'message': 'Pedido não encontrada'}), 404

# Endpoint para atualizar um pedido pelo ID
@app.route('/pedidos/<int:idPedido>', methods=['PUT'])
def update_pedido(idPedido):
    pedido = Pedido.query.get(idPedido)
    if not pedido:
        return jsonify({'message': 'Pedido não encontrado'}), 404
    data = request.get_json()

    pedido.idRota = data['idRota']
    pedido.nomeCliente = data['nomeCliente']
    pedido.endereco = data['endereco']
    pedido.observacoes = data['observacoes']
    pedido.telefone = data['telefone']
    pedido.itensPedido = json.dumps(data['itensPedido'])
    pedido.statusEntrega = data['statusEntrega']
    pedido.observacoesEntrega = data['observacoesEntrega']

    db.session.commit()
    return jsonify({'message': 'Pedido atualizado com sucesso!'})

# Endpoint para excluir um Pedido pelo ID
@app.route('/pedidos/<int:idPedido>', methods=['DELETE'])
def delete_pedido(idPedido):
    pedido = Pedido.query.get(idPedido)
    if not pedido:
        return jsonify({'message': 'Pedido não encontrado'}), 404
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'message': 'Peiddo excluído com sucesso!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)