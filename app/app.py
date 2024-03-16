# Import the Flask class from the Flask library
from flask import Flask

# Create a Flask application instance named 'app'
app = Flask(__name__)

# Define a function called 'hello' to handle requests to the root URL ('/')
@app.route('/')
def hello():
    # Return the response string "Hola desde Flask!"
    return "Hola desde Flask!"

# If the script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Start the development server on localhost:5000, accessible from any device on the network
    app.run(host='0.0.0.0', port=5000)
