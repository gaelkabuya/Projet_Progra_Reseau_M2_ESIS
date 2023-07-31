from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialisation des données
flights = {
    1: {'id': 1, 'compagnie': 'congo_airways', 'depart': 'kinshasa', 'arrivée': 'likasi'},
    2: {'id': 2, 'compagnie': 'caa', 'depart': 'kolwezi', 'arrivée': 'lubumbashi'}
}

passengers = {
    1: {'id': 1, 'name': 'victoire', 'email': 'victoire@esis.com', 'phone': '1001', 'flight_id': 1},
    2: {'id': 2, 'name': 'gomer', 'email': 'gomer@esis.com', 'phone': '1002', 'flight_id': 2}
}

# Routes pour les vols
@app.route('/flights', methods=['GET'])
def get_flights():
    return jsonify(flights)

@app.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight(flight_id):
    if flight_id in flights:
        return jsonify(flights[flight_id])
    else:
        return jsonify({'error': 'Le vol n a pas été trouvé'})

@app.route('/flights', methods=['POST'])
def add_flight():
    data = request.get_json()
    flight_id = data['id']
    if flight_id not in flights:
        flights[flight_id] = data
        return jsonify({'message': 'Vol ajouté avec succès'})
    else:
        return jsonify({'error': 'Le vol exixte déja'})

@app.route('/flights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
    if flight_id in flights:
        data = request.get_json()
        flights[flight_id]['compagnie'] = data['compagnie']
        flights[flight_id]['depart'] = data['depart']
        flights[flight_id]['arrivée'] = data['arrivée']
        return jsonify({'message': 'Le vol a été mis à jour'})
    else:
        return jsonify({'error': 'Flight not found'})

@app.route('/flights/<int:flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    if flight_id in flights:
        del flights[flight_id]
        return jsonify({'message': 'Le vol a été supprimé'})
    else:
        return jsonify({'error': 'Ce vol est introuvable'})

# Routes pour les passagers
@app.route('/passengers', methods=['GET'])
def get_passengers():
    return jsonify(passengers)

@app.route('/passengers/<int:passenger_id>', methods=['GET'])
def get_passenger(passenger_id):
    if passenger_id in passengers:
        return jsonify(passengers[passenger_id])
    else:
        return jsonify({'error': 'Passenger not found'})

@app.route('/passengers', methods=['POST'])
def add_passenger():
    data = request.get_json()
    passenger_id = data['id']
    if passenger_id not in passengers:
        passengers[passenger_id] = data
        return jsonify({'message': 'Passenger added successfully'})
    else:
        return jsonify({'error': 'Passenger already exists'})

@app.route('/passengers/<int:passenger_id>', methods=['PUT'])
def update_passenger(passenger_id):
    if passenger_id in passengers:
        data = request.get_json()
        passengers[passenger_id]['name'] = data['name']
        passengers[passenger_id]['email'] = data['email']
        passengers[passenger_id]['phone'] = data['phone']
        passengers[passenger_id]['flight_id'] = data['flight_id']
        return jsonify({'message': 'Passenger updated successfully'})
    else:
        return jsonify({'error': 'Passenger not found'})

@app.route('/passengers/<int:passenger_id>', methods=['DELETE'])
def delete_passenger(passenger_id):
    if passenger_id in passengers:
        del passengers[passenger_id]
        return jsonify({'message': 'Passenger deleted successfully'})
    else:
        return jsonify({'error': 'Passenger not found'})

if __name__ == '__main__':
    app.run(debug=True)