import os
from flask import Flask
from application import generator

app = Flask(__name__)


@app.route('/')
def generate_buzz():
    html = "<html><body><h1>"
    html += generator.generate_buzz()
    html += "</h1></body></html>"
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
