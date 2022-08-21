from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient

fandiary_bp = Blueprint('fandiary_bp', __name__,
    template_folder='templates',
    static_folder='static', url_prefix='/fandiary')


client = MongoClient('mongodb+srv://banhyungil:qudduqdl1!@cluster0.umvvk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@fandiary_bp.route('/')
def home():
  return render_template('/fandiary/fandiary.html')

@fandiary_bp.route('/load', methods=['GET'])
def load():
  return select_fan_cmt_list()

# fan 응원 목록 조회
def select_fan_cmt_list():
  fan_cmt_list = list(db.fan.find({}, {'_id': False}))
  
  return jsonify({'fan_cmt_list':fan_cmt_list})


@fandiary_bp.route('/save', methods=['POST'])
def save_fan_cmt():
  userNm = request.form['userNm']
  comment = request.form['comment']
  
  doc = {
    'userNm': userNm,
    'comment': comment
  }
  
  db.fan.insert_one(doc)
  return jsonify({'msg':'저장완료!'})
