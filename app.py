from flask import Flask, render_template, request
import jsonify 
import sklearn
import pickle 

app = Flask(__name__)

model = pickle.load(open("C:/Users/Lenovo/Desktop/Visual Studio/end to end/car_price_prediction/model.pkl",'rb'))

@app.route('/', methods = ['GET'])
def index() : 
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict() : 
    
    if request.method == 'POST' : 
        
        year = int(request.form['year'])
        present_price = float(request.form['present_price'])
        kms_driven = int(request.form['kms_driven'])
        owner = request.form['owners']
        seller_type = request.form['seller_type']
        transmission = request.form['transmission']
        fuel_type = request.form['fuel_type']

        if seller_type == 'Dealer' : 
            seller_type = 1
        else : 
            seller_type = 0

        if transmission == "Manual" : 
            transmission = 1
        else : 
            transmission = 0 

        if fuel_type == 'Petrol' : 
            fuel_type = 1
        elif fuel_type == 'Diesel' : 
            fuel_type = 0 
        else : 
            fuel_type = 2

        prediction = model.predict([[year, present_price, kms_driven, fuel_type, seller_type, transmission, owner]])

        if prediction < 0 : 
            return render_template('index.html', prediction_value = "Sorry you can't sell this car")
        
        else : 
            return render_template('index.html', prediction_value = "Your car selling price is {}".format(prediction[0]))

    else : 
        return render_template('index.html')

if __name__ == "__main__" : 
    app.run(debug=True)