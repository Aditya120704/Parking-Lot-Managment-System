from flask import Flask, jsonify, request, render_template
from parking_system.core import ParkingLot

app = Flask(__name__)
parking_lot = ParkingLot(capacity=3)  # Initialize with default capacity

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/park', methods=['POST'])
def park_vehicle():
    data = request.json
    vehicle_number = data.get('vehicle_number')
    if not vehicle_number:
        return jsonify({"error": "Vehicle number is required"}), 400
    result = parking_lot.park_vehicle(vehicle_number)
    return jsonify({"message": result})

@app.route('/api/remove', methods=['POST'])
def remove_vehicle():
    data = request.json
    vehicle_number = data.get('vehicle_number')
    if not vehicle_number:
        return jsonify({"error": "Vehicle number is required"}), 400
    result = parking_lot.remove_vehicle(vehicle_number)
    return jsonify({"message": result})

@app.route('/api/status', methods=['GET'])
def get_status():
    status = parking_lot.get_status()
    return jsonify(status)

if __name__ == '__main__':
    app.run(debug=True)
