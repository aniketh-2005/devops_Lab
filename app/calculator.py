from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@app.route('/add', methods=['GET'])
def add_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({'result': add(a, b)})

@app.route('/subtract', methods=['GET'])
def subtract_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({'result': subtract(a, b)})

@app.route('/multiply', methods=['GET'])
def multiply_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({'result': multiply(a, b)})

@app.route('/divide', methods=['GET'])
def divide_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    try:
        result = divide(a, b)
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
