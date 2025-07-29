from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def create_order():
    users = requests.get('http://user-service:5000/users').json()
    products = requests.get('http://product-service:5001/products').json()
    return jsonify({
        "order_id": 1,
        "user": users[0],
        "product": products[0]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
