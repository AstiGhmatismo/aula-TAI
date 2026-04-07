from flask import Flask, jsonify, request

app = Flask(__name__)



class Pokemon:
    def __init__(self, nome, tipo, tipo2, apelido):
        self.nome = nome
        self.tipo = tipo
        self.tipo2 = tipo2
        self.apelido = apelido

    def to_dict(self):
        return self.__dict__

class Treinador:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.time = []

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "time": [p.to_dict() for p in self.time]
        }


db_treinadores = {}

@app.after_request
def add_cors_headers(response):
    response.headers["Acess-Control-Allow-Origin"] = "*"
    response.headers["Acess-Control-Allow-Origin"] = "GET, POST, OPTIONS"
    response.headers["Acess-Control-Allow-Origin"] = "Content-Type"
    return response

@app.route('/treinadores', methods=['GET', 'POST'])
def colecao_treinadores():
    if request.method == 'GET':
       
        lista = [t.to_dict() for t in db_treinadores.values()]
        return jsonify(lista), 200

    if request.method == 'POST':
        dados = request.json
        nome = dados.get('nome')
        
        if not nome:
            return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400
        
        if nome in db_treinadores:
            return jsonify({"erro": "Treinador já cadastrado"}), 409
        
        
        novo = Treinador(nome, dados.get('idade'))
        db_treinadores[nome] = novo
        return jsonify({"msg": f"Treinador {nome} criado com sucesso!"}), 201


@app.route('/treinadores/<nome_id>', methods=['PUT', 'DELETE'])
def elemento_treinador(nome_id):
    if nome_id not in db_treinadores:
        return jsonify({"erro": "Treinador não encontrado"}), 404

    if request.method == 'PUT':
        dados = request.json
        novo_nome = dados.get('nome')
        nova_idade = dados.get('idade')
        
        treinador = db_treinadores[nome_id]
        if nova_idade:
            treinador.idade = nova_idade
            
        
        if novo_nome and novo_nome != nome_id:
            treinador.nome = novo_nome
            db_treinadores[novo_nome] = db_treinadores.pop(nome_id)
            return jsonify({"msg": "Nome e dados atualizados!"}), 200
            
        return jsonify({"msg": "Dados atualizados!"}), 200

    if request.method == 'DELETE':
        del db_treinadores[nome_id]
        return jsonify({"msg": f"Treinador {nome_id} removido do sistema"}), 200


@app.route('/treinadores/<nome_id>/pokemon', methods=['POST'])
def capturar_pokemon(nome_id):
    if nome_id not in db_treinadores:
        return jsonify({"erro": "Treinador não existe"}), 404
    
    dados = request.json
   
    if len(db_treinadores[nome_id].time) >= 6:
        return jsonify({"erro": "O time já está cheio (limite 6)"}), 400

    novo_poko = Pokemon(
        nome=dados.get('nome'),
        tipo=dados.get('tipo'),
        tipo2=dados.get('tipo2'),
        apelido=dados.get('apelido')
    )
    
    db_treinadores[nome_id].time.append(novo_poko)
    return jsonify({"msg": f"{novo_poko.nome} adicionado ao time de {nome_id}!"}), 201

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)