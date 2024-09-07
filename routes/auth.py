from flask import Blueprint, render_template, redirect, url_for, request, flash
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission (you'll need your own logic here)
        username = request.form['username']
        password = request.form['password']
         
        if username == "test" and password == "test":  # Placeholder logic
            print('Login successful!')
            return redirect(url_for('home.index'))
        else:
            print('Invalid credentials, try again.')
    
    return render_template('auth/login.html')

# Route for signup page
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup form submission (you'll need your own logic here)
        username = request.form['username']
        password = request.form['password']
        # Add logic to create a new user
        flash('Signup successful!')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/signup.html')
