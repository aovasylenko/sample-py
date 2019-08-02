from flask import Flask
from uuid import uuid4
from datetime import datetime
application = Flask(__name__)

@application.route("/<route>")
def hello(route):
    time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
    request_id = str(uuid4())
    print("[{}][INFO   ][MainProcess][Thread-3 ][main.py:66][id:{}] Log message: {}".format(time, request_id, route))
    print("[{}][WARNING][MainProcess ][Thre-3   ][main.py:66][id:] Log message: {}".format(time, route))
    print("[{}][WARNING][MainProcess ][Thre-3   ][main.py:66][id:]".format(time))

    return "Just a test"

if __name__ == "__main__":
    application.run()