from flask import Flask, render_template
from fandiary.fandiary_bp import fandiary_bp
from bucket.bucket_bp import bucket_bp
from mars.mars_bp import mars_bp
from movie_cinema.movie_cinema_bp import movie_cinema_bp

app = Flask(__name__)
app.register_blueprint(fandiary_bp)
app.register_blueprint(bucket_bp)
app.register_blueprint(mars_bp)
app.register_blueprint(movie_cinema_bp)


@app.route('/')
def home():
    return render_template('/fandiary/fandiary.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000",debug=True)