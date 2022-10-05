from flask import Flask, render_template

from maini import load_data

ap = Flask(__name__)


@ap.route('/home')
def products_page():
    data_collecting = load_data("products.json")
    return render_template("product.html", data_collecting=data_collecting)


if __name__ == '__main__':
    ap.run()
