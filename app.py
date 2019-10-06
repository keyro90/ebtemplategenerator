import os
from flask import Flask, request, abort, jsonify
from werkzeug.exceptions import BadRequest
from classes.EventbriteDispatcher import EventbriteDispatcher

app = Flask(__name__)

@app.route('/tlevents', methods=['GET'])
def hello_world():
    ev = EventbriteDispatcher()
    ev.get_all_events()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
