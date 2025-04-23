from flask import Flask, request, jsonify

app = Flask(__name__)

# Core operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# API route for addition
@app.route('/add', methods=['GET','POST'])
def handle_add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = add(a, b)
    return jsonify({'operation': 'add', 'a': a, 'b': b, 'result': result})

# API route for subtraction
@app.route('/subtract', methods=['GET', 'POST'])
def handle_subtract():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = subtract(a, b)
    return jsonify({'operation': 'subtract', 'a': a, 'b': b, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
