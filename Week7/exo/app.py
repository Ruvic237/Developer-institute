from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def welcome():  # put application's code here
#     return "Hello don't doubt"
#
#
# @app.route('/blog')
# def blog():  # put application's code here
#     return render_template('homepage.html', name = "Ruvic")
#
#
# @app.route('/blog/articles')
# def article():  # put application's code here
#     return render_template('article.html', dict = {"School": "Pencil", "Technology": "laptop"})

@app.route('/')
def blog():  # put application's code here
    return render_template('homepage.html', name = "Ruvic")


@app.route('/blog/articles')
def article():  # put application's code here
    return render_template('article.html', dict = {"title": "Avengers", "Content": "Fantasy", "author": "Keng"})


if __name__ == '__main__':
    app.run()

    
