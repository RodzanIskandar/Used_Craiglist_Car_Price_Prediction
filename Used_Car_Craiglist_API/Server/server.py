from flask import Flask, jsonify, request
import util

app = Flask(__name__)

@app.route('/get_manufacturer')
def get_manufacturer():
    response = jsonify({'manufacturer': util.get_manufacturer()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_condition')
def get_condition():
    response = jsonify({'condition': util.get_condition()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_cylinders')
def get_cylinders():
    response = jsonify({'cylinders': util.get_cylinders()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_fuel')
def get_fuel():
    response = jsonify({'fuel': util.get_fuel()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_transmission')
def get_transmission():
    response = jsonify({'transmission': util.get_transmission()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_drive')
def get_drive():
    response = jsonify({'drive': util.get_drive()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_type')
def get_type():
    response = jsonify({'type': util.get_type()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_car_size')
def get_car_size():
    response = jsonify({'car_size': util.get_car_size()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/UCC_predict', methods=['POST'])
def UCC_predict():
    manufacturer = request.form['manufacturer']
    condition = request.form['condition']
    cylinders = request.form['cylinders']
    fuel = request.form['fuel']
    odometer = int(request.form['odometer'])
    transmission = request.form['transmission']
    drive = request.form['drive']
    type = request.form['type']
    age = int(request.form['age'])
    car_size = request.form['car_size']

    response = jsonify({'predicted_price': util.predicted_price(manufacturer, condition, cylinders, fuel, odometer, transmission, drive, type, age, car_size)})

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print('starting Python Flask Server for Used car Craiglist Prediction...')
    util.load_saved_data()
    app.run()