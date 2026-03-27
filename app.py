from flask import Flask, render_template, request
from controller import get_movies, get_recommendations

app = Flask(__name__)

# @app.route('/')
# def index():
#     movies = get_movies()
#     return render_template('index.html', movie_list=movies)

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     movie = request.form['movie']
#     recommendations = get_recommendations(movie)
#     movies = get_movies()
#     return render_template(
#         'index.html',
#         movie_list=movies,
#         recommendations=recommendations
#     )

@app.route('/')
def index():
    movies = get_movies()
    return render_template('index.html', movie_list=movies, selected_movie=None)


@app.route('/recommend', methods=['POST'])
def recommend():
    movie = request.form['movie']
    recommendations = get_recommendations(movie)
    movies = get_movies()

    return render_template(
        'index.html',
        movie_list=movies,
        recommendations=recommendations,
        selected_movie=movie   # ✅ important
    )

@app.errorhandler(404)
def not_found(e):
    return render_template(
        'error.html',
        error_code=404,
        error_message="Page not found"
    ), 404


@app.errorhandler(500)
def server_error(e):
    return render_template(
        'error.html',
        error_code=500,
        error_message="Internal server error"
    ), 500


@app.errorhandler(400)
def bad_request(e):
    return render_template(
        'error.html',
        error_code=400,
        error_message="Bad request"
    ), 400



if __name__ == '__main__':
    app.run(debug=True)