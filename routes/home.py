from flask import Blueprint, render_template, redirect, url_for, request, flash
home_bp = Blueprint('auth', __name__)

@home_bp.route('/',methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@home_bp.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Capture the form data
        category = request.form['category']
        device_type = request.form['device_type']
        brand = request.form['brand']
        model = request.form['model']
        condition = request.form['condition']
        return render_template('home/result.html', price="predicted_price")
    
    return redirect(url_for('home.index'))
