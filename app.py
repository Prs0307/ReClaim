from __init__ import create_app

# Create an application instance
app = create_app()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)