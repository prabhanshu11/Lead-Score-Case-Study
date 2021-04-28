import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from forms import RegisterForm
from form_predict import form_predict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'prabhu'


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home_page():
    form = RegisterForm()
    if form.validate_on_submit():
        data = [
            form.visits.data,
            form.time_minutes.data,
            form.source.data,
            form.is_professional.data
        ]
        if form_predict(data): 
            prediction = "The lead may Convert"
        else: prediction = "The lead might not Convert"
        return render_template('index_bootstrap.html',form=form, prediction=prediction)
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)
    #
    #output = round(prediction[0], 2)
    #output = sum(int_features)
    #return render_template('index.html', 
    #               prediction_text=f'Employee Salary should be $ {output}')
    return render_template('index_bootstrap.html', form=form)

@app.route('/metrics')
def metrics_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('metrics.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)
