# Import necessary modules
from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

# Define two API endpoints
@app.route('/', methods=['GET'])
def hi():
    return jsonify(message="Use /hello or /goodbye")

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

@app.route('/goodbye', methods=['GET'])
def goodbye():
    return jsonify(message="Goodbye, World!")

@app.route('/test1', methods=['GET'])
def test1():
    return jsonify(message="Test1 is OK")

@app.route('/test1', methods=['GET'])
def test2():
    return jsonify(message="Test2 is OK")

# Run the app if executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
