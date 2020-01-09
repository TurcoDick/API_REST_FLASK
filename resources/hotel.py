from flask_restful import Resource, reqparse

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


class Hotel(Resource):

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message' : 'Hotel not found. '}, 404

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')

        dados = argumentos.parse_args()

        novo_hotel = {
            'hotel_id' : hotel_id,
            'nome' : dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria' : dados['diaria'],
            'cidade' : dados['cidade']
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            pass
        else:
            Hotel.post(hotel_id)

    def delete(self, hotel_id):
        pass
