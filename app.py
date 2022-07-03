from flask import Flask, jsonify, request

from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML

from schema.create import create_schema

from data import all_authors, all_blogs, get_author, get_blog, update_blog , Blog, Author

app = Flask(__name__)

'''
Graph QL
'''
@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route('/graphql', methods=['POST'])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    schema = create_schema()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code

'''
Flask
'''
@app.route('/')
def route_hello_world():
    return "Hello World"

@app.route('/blogs')
def route_all_blogs():
    return jsonify(all_blogs())

@app.route('/blogs/<id>', methods=['GET'])
def route_get_blog(id: str):
    return jsonify(get_blog(int(id)))


@app.route('/blogs/<id>', methods=['POST'])
def route_update_blog(id: str):
    payload = request.get_json()

    return(jsonify(update_blog(int(id), payload)))

@app.route("/authors")
def route_all_authors():
    return jsonify(all_authors())

@app.route("/authors/<id>", methods=['GET'])
def route_get_author(id: str):
    return jsonify(get_author(int(id)))

if __name__ == '__main__':
    app.run()