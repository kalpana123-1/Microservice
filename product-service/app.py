from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 75000},
        {"id": 2, "name": "Phone", "price": 25000}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
