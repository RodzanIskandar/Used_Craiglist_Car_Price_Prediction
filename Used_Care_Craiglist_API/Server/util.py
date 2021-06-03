import json
import pickle
import numpy as np

__data_percolumns = None
__manufacturer = None
__condition = None
__cylinders = None
__fuel = None
__transmission = None
__drive = None
__type = None
__car_size = None
__model = None
__LabelEncoder = None
__scaler = None

def predicted_price(manufacturer, condition, cylinders, fuel, odometer, transmission, drive, type, age, car_size):
    
    x = np.zeros(10)
    x[0] = __LabelEncoder['manufacturer'].transform([manufacturer])
    x[1] = __LabelEncoder['condition'].transform([condition])
    x[2] = __LabelEncoder['cylinders'].transform([cylinders])
    x[3] = __LabelEncoder['fuel'].transform([fuel])
    x[4] = odometer
    x[5] = __LabelEncoder['transmission'].transform([transmission])
    x[6] = __LabelEncoder['drive'].transform([drive])
    x[7] = __LabelEncoder['type'].transform([type])
    x[8] = age
    x[9] = __LabelEncoder['car_size'].transform([car_size])
    
    x = __scaler.transform([x])
    
    
    return round(__model.predict(x)[0],2)

def get_manufacturer():
    return __manufacturer
def get_condition():
    return __condition
def get_cylinders():
    return __cylinders
def get_fuel():
    return __fuel
def get_transmisson():
    return __transmission
def get_drive():
    return __drive
def get_type():
    return __type
def get_car_size():
    return __car_size

def load_saved_data():
    print('loading saved data...start')
    global __data_percolumns
    global __manufacturer
    global __condition
    global __cylinders
    global __fuel
    global __transmission
    global __drive
    global __type
    global __car_size


    with open("./Server/saved data/data_ucc.json", 'r') as f:
        __data_percolumns = json.load(f)
        __manufacturer = __data_percolumns['data_manufacturer']
        __condition = __data_percolumns['data_condition']
        __cylinders = __data_percolumns['data_cylinders']
        __fuel = __data_percolumns['data_fuel']
        __transmission = __data_percolumns['data_transmission']
        __drive = __data_percolumns['data_drive']
        __type = __data_percolumns['data_type']
        __car_size = __data_percolumns['data_car_size']

    
    global __model
    with open("./Server/saved data/used_car_craiglist_model_prediction.pickle", 'rb') as f:
        __model = pickle.load(f)
    
    global __LabelEncoder
    with open("./Server/saved data/label_encoder_ucc.pickle", 'rb') as f:
        __LabelEncoder = pickle.load(f)

    global __scaler
    with open('./Server/saved data/scaler_ucc.pickle', 'rb') as f:
        __scaler = pickle.load(f)

    print('loading saved data...done')   

if __name__ == '__main__':
    load_saved_data()
    #print(get_manufacturer())
    #print(get_condition())
    #print(get_cylinders())
    #print(get_fuel())
    #print(get_transmisson())
    #print(get_drive())
    #print(get_type())
    #print(get_car_size())
    print(predicted_price('toyota', 'excellent', '8 cylinders', 'gas', 1000000.0 , 'automatic', 'rwd', 'sedan', 20, 'mid-size'))