from flask import Flask , render_template, request, url_for
import csv
from datetime import datetime
import joblib
model = joblib.load('model.joblib')
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/history')
def history():
    history = []
    try:
        with open('prediction_history.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                history.append(row)
    except FileNotFoundError:
        pass
    return render_template('history.html', history=history)

@app.route('/project', methods = ["POST","GET"])
def predict():
    if request.method=='POST':
        brand_name=request.form['brand_name']
        owner = request.form['owner']
        age = request.form['age']
        power = request.form['power']
        kms_driven=request.form['kms_driven']

        brand_dict = {
            'TVS':1,
            'Royal Enfield':2,
            'Triumph':3,
            'Yamaha':4,
            'Honda':5,
            'Hero':6,
            'Bajaj':7,
            'Suzuki':8,
            'Benelli':9,
            'KTM':10,
            'Mahindra':11,
            'Kawasaki':12,
            'Ducati':13,
            'Hyosung':14,
            'Harley-Davidson':15,
            'Jawa':16,
            'BMW':17,
            'Indian':18,
            'Rajdoot':19,
            'LML':20,
            'Yezdi':21,
            'MV':22,
            'Ideal':23
        }

        brand_code = brand_dict[brand_name]
        owner_int = int(owner)
        age_int = float(age)
        power_float = float(power)
        kms_driven_float = float(kms_driven)
        lst = [[brand_code, owner_int, age_int, power_float, kms_driven_float]]
        prediction = model.predict(lst)
        rounded_prediction = round(prediction[0], 2)
        print("prediction:-", prediction)

        # Save prediction to CSV
        row = {
            'brand_name': brand_name,
            'owner': owner,
            'age': age,
            'power': power,
            'kms_driven': kms_driven,
            'prediction': rounded_prediction,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        file_exists = False
        try:
            with open('prediction_history.csv', 'r', encoding='utf-8') as f:
                file_exists = True
        except FileNotFoundError:
            pass
        with open('prediction_history.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['brand_name', 'owner', 'age', 'power', 'kms_driven', 'prediction', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(row)

        return render_template('project.html', prediction=rounded_prediction, 
            brand_name=brand_name,
            owner=owner,
            age=age,
            power=power,
            kms_driven=kms_driven)

    return render_template('project.html')


#     brand_dict= dt2[brand_name]
#     data = [[brand_name,owner,age,power,kms_driven]]
    


if __name__ == "__main__":
    app.run(debug = True)


# 🙋‍♂️ Developed By

#**Rahul Parihar**  
#🎓 B-tech Student @ BTU University, Bikaner