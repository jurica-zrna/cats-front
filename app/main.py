import sys
import random
import os
import logging
from flask import Flask, render_template, make_response
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

host = os.getenv('HOSTNAME', 'localhost')
api_url = os.getenv('API_URL', 'localhost:8080/api/CatBreed')
static_url = os.getenv('STATIC_URL', 'localhost:9090/images')
title = ("Cat facts")

@app.route('/')
def index():
    response = make_response(render_template('index.html', title=title, host=host, CatBreed_api_url = api_url, static_files_url = static_url))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
