from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
products = []

@app.route('/')
def home():
    return "Welcome to Retail App"

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    products.append(data)
    return jsonify({"message": "Product added!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
