import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify, Blueprint
from pymongo import MongoClient

movie_cinema_bp = Blueprint('movie_cinema_bp', __name__,
                            static_folder='static',
                            template_folder='templates', url_prefix='/movieCinema')

client = MongoClient('mongodb+srv://banhyungil:qudduqdl1!@cluster0.umvvk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

res = requests.get('https://movie.naver.com/movie/bi/mi/basic.naver?code=191597')
soup = BeautifulSoup.find

@movie_cinema_bp.route('/')
def home():
    return render_template('movie_cinema/movie_cinema.html')

@movie_cinema_bp.route("/movie", methods=["POST"])
def post_movie():
    req = request.form  # url, star, comment
    print(req)

    res = requests.get(req['url'])
    soup = BeautifulSoup(res.text, 'html.parser')

    craw_title = soup.select_one('meta[property="og:title"]')['content']
    craw_image = soup.select_one('meta[property="og:image"]')['content']
    craw_desc = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'title': craw_title,
        'image': craw_image,
        'desc': craw_desc,
        'star': req['star'],
        'comment': req['comment']
    }
    print(doc)
    db.movies.insert_one(doc)

    return jsonify({'msg': '저장 완료'})

@movie_cinema_bp.route("/movie", methods=["GET"])
def select_movies():
    # db에서 영화 정보를 읽어 반환한다.
    movies = list(db.movies.find({}, {'_id':0}))

    return jsonify(movies)