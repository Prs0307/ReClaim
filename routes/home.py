from flask import Blueprint, render_template, redirect, url_for, request
home_bp = Blueprint('auth', __name__)




@home_bp.route('/')
def index():
    return render_template('home.html')


@home_bp.route('/result', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Capture the form data
        category = request.form['category']
        device_type = request.form['device_type']
        brand = request.form['brand']
        model = request.form['model']
        condition = request.form['condition']
        print(category, device_type,brand, model, condition)
        # Perform your prediction logic here
        # Replace "predicted_price" with the actual predicted price
        predicted_price = calculate_price(category, device_type, brand, model, condition)

        return render_template('result.html', price=predicted_price)
    return redirect(url_for('home.html'))

def calculate_price(category, device_type, brand, model, condition):
 
    predicted_price = 1000  # Placeholder value

    return predicted_price