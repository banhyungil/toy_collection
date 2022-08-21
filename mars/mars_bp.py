from flask import Flask, render_template, request, jsonify, Blueprint
from pymongo import MongoClient


mars_bp = Blueprint('mars_bp', __name__,
                    template_folder='templates',
                    static_folder='static', url_prefix='/mars')

client = MongoClient('mongodb+srv://banhyungil:qudduqdl1!@cluster0.umvvk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@mars_bp.route('/')
def home():
    return render_template('/mars/mars.html')


@mars_bp.route("/mars", methods=["POST"])
def web_mars_post():
    req = request.form
    doc = {
        'name': req['name'],
        'address': req['address'],
        'size': req['size']
    }
    print(doc)
    db.mars.insert_one(doc)
    return jsonify({'msg': '주문완료!!!'})


@mars_bp.route("/mars", methods=["GET"])
def select_mars():
    order_list = list(db.mars.find({}, {'_id': False}))
    for order in order_list:
        print(order)

    return jsonify(order_list)

data = {'abc':'name',
        'hi':'say',
        }

