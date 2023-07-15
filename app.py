from flask import Flask, request, jsonify
from goose3 import Goose

app = Flask(__name__)

@app.route('/extract_description', methods=['POST'])
def extract_description():
    url = request.json['url']

    # Use Goose to extract the description from the provided URL
    g = Goose()
    article = g.extract(url=url)
    description = article.meta_description

    return jsonify({'description': description})

if __name__ == '__main__':
    app.run()
