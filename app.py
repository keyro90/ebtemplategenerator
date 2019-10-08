import os
from flask import Flask, request, abort, jsonify, render_template
from werkzeug.exceptions import BadRequest
from classes.EventbriteDispatcher import EventbriteDispatcher

app = Flask(__name__)


@app.route('/tlevents', methods=['GET'])
def hello_world():
    ev = EventbriteDispatcher()
    all_events = ev.get_all_events()
    simple_events = []
    print(all_events)
    for single_ev in all_events["events"]:
        simple_events.append(
            {"event_title": single_ev["name"]["text"], "event_logo": single_ev["logo"]["original"]["url"],
             "event_description": single_ev["summary"], "event_url": single_ev["url"]})
    return render_template("index.html", len=len(simple_events), AllEvents=simple_events)


if __name__ == '__main__':
    app.run()
