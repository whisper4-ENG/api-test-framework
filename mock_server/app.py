from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = "test_token"
products = [
    {
        "id": 1,
        "name": "iPhone 16",
        "price": 6999
    },
    {
        "id": 2,
        "name": "MacBook Pro",
        "price": 14999
    }
]

orders = []

@app.route("/products", methods=["GET"])
def product_list():

    return jsonify({
        "code": 200,
        "data": products
    })

@app.route("/order/create", methods=["POST"])
def create_order():

    token = request.headers.get("Authorization")

    if token != TOKEN:

        return jsonify({
            "code": 403,
            "msg": "invalid token"
        })

    data = request.json

    order = {
        "order_id": len(orders) + 1,
        "product_id": data["product_id"],
        "quantity": data["quantity"]
    }

    orders.append(order)

    return jsonify({
        "code": 200,
        "msg": "success",
        "data": order
    })

@app.route("/order/detail/<int:order_id>", methods=["GET"])
def query_order(order_id):

    for order in orders:

        if order["order_id"] == order_id:
            return jsonify({
                "code": 200,
                "data": order
            })

    return jsonify({
        "code": 404,
        "msg": "not found"
    })

    data = request.json

    order = {
        "order_id": len(orders) + 1,
        "product_id": data["product_id"],
        "quantity": data["quantity"]
    }

    orders.append(order)

    return jsonify({
        "code": 200,
        "data": order
    })

@app.route("/login", methods=["POST"])
def login():

    data = request.json

    if (
            data["username"] == "admin"
            and
            data["password"] == "123456"
    ):

        return jsonify({
            "code": 200,
            "token": TOKEN
        })

    return jsonify({
        "code": 401,
        "msg": "用户名或密码错误"
    })


@app.route("/user/info", methods=["GET"])
def user_info():

    token = request.headers.get("Authorization")

    if token == TOKEN:

        return jsonify({
            "code": 200,
            "data": {
                "id": 1,
                "username": "admin",
                "email": "admin@test.com"
            }
        })

    return jsonify({
        "code": 403,
        "msg": "invalid token"
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )