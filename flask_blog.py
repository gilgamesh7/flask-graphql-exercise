from webbrowser import get
from flask import Flask, jsonify

from data import all_authors, all_blogs, get_author, get_blog, update_blog

app = Flask(__name__)

@app.route('/')
def route_hello_world():
    return "Hello World"

@app.route('/blogs')
def route_all_blogs():
    return jsonify(all_blogs())

@app.route('/blogs/<id>', methods=['GET'])
def route_get_blog(id: str):
    return jsonify(all_blogs())

@app.route("/authors")
def route_all_authors():
    return jsonify(all_authors())

@app.route("/authors/<id>", methods=['GET'])
def route_get_author(id: str):
    return jsonify(get_author(int(id)))

if __name__ == '__main__':
    app.run()