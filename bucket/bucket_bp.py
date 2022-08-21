from http import client
from flask import Flask, render_template, request, json, jsonify, Blueprint
from bson import json_util
from pymongo import MongoClient
from bson.objectid import ObjectId


bucket_bp = Blueprint('bucket_bp', __name__,
                      template_folder='templates',
                      static_folder='static', url_prefix='/bucket')

client = MongoClient('mongodb+srv://banhyungil:qudduqdl1!@cluster0.umvvk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@bucket_bp.route('/')
def home():
  return render_template('/bucket/bucket.html')

@bucket_bp.route("/saveBucket", methods=["POST"])
def bucket_post():
  bucket = request.form['bucket']
  doc = {
    'bucket': bucket,
    'isDone': False
  }
  
  db.bucket.insert_one(doc)
  
  return jsonify({'msg': '버킷 등록완료'})

@bucket_bp.route("/saveBucket/done", methods=["POST"])
def bucket_done():
  taget_objectId = request.form['objectId']
  
  db.bucket.update_one({'_id': ObjectId(taget_objectId)}, {'$set':{'isDone': True}})
                       
  return jsonify({'msg': '할일 완료!'})

@bucket_bp.route("/selectBucket", methods=["GET"])
def selectBucket():
  data = list(db.bucket.find({}))  # bson 반환, 2번쨰 인자는 제외할 field dictionary
  
  return {'bucket_list':parse_json(data)};

# bson to json
def parse_json(data):
  return json.loads(json_util.dumps(data))
  