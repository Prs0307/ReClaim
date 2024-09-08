from flask import redirect, render_template, request, url_for
from __init__ import create_app

# Create an application instance
app = create_app()

# By Dinkar
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template('result.html')
@app.route('/address', methods=['GET', 'POST'])
def address():
    return render_template('user_detail.html')
@app.route('/submit-details', methods=['GET', 'POST'])
def submitdetails():
    return render_template('nearby_shop.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)