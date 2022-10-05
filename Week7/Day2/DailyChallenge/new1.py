from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def link():
    return render_template("Home.html")


@app.route('/blue')
def blue():
    return render_template("blue.html")


@app.route('/red')
def red():
    return render_template("red.html")


@app.route('/green')
def green():
    return render_template("green.html")


@app.route('/yellow')
def yellow():
    return render_template("yellow.html")


if __name__ == '__main__':
    app.run(debug=True)
