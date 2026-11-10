import os
import json
import datetime
from flask import Flask, jsonify

app = Flask(__name__)

# Locate news_data.json relative to backend.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'news_data.json')

@app.route('/news.all.get')
def get_news_all_articles():
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    app.logger.debug('_________________Hello ' + str(data))
    return jsonify(data)

@app.route('/news.categories.get')
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'title': 'List of Categories',
        'time': time_now_str,
        'categories': [
            {'id': 1, 'name': 'Sports'},
            {'id': 2, 'name': 'Politics'},
            {'id': 3, 'name': 'Education'}
        ]
    }
    return jsonify(data)

@app.route('/')
def index():
    return 'Welcome ENSIA Students from Flask!'

if __name__ == "__main__":
    app.run(port=8080)