from flask_restful import Resource

hoteis = [
    {
        'hotel_id' : 'alpha',
        'nome' : 'Alpha hotel',
        'estrelas' : 4.3,
        'diaria' : 399.32,
        'cidade' : 'Campos do Jordão'
    },
    {
        'hotel_id' : 'minion',
        'nome' : 'minion hotel',
        'estrelas' : 4.5,
        'diaria' : 3933.77,
        'cidade' : 'São jose dos Campos'
    },
    {
        'hotel_id' : 'balofo',
        'nome' : 'balofo hotel',
        'estrelas' : 4.9,
        'diaria' : 799.32,
        'cidade' : 'São Bneto do Sapucai'
    },
    {
        'hotel_id' : 'rufos',
        'nome' : 'rufos hotel',
        'estrelas' : 3.3,
        'diaria' : 199.32,
        'cidade' : 'Taubate'
    },
    {
        'hotel_id' : 'apolo',
        'nome' : 'apolo hotel',
        'estrelas' : 4.8,
        'diaria' : 5799.32,
        'cidade' : 'bento Gonsalvez'
    }
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis' : hoteis}

    def put(self):
       pass

    def delete(self):
        pass