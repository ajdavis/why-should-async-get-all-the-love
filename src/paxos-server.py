import json
import time
import uuid
from concurrent.futures import Future, ThreadPoolExecutor

import flask
import requests

server_id = uuid.uuid4().hex
app = flask.Flask('PyPaxos')
self_future = Future()

@app.route('/server_id', methods=['GET'])
def get_server_id():
    return flask.jsonify(server_id)

@app.route('/client-request', methods=['POST'])
def client_request():
    self_future.result()
    ...

config = json.load(open("paxos-config.json"))
executor = ThreadPoolExecutor()
app_done = executor.submit(lambda: app.run(host="0.0.0.0", port=9999))

start = time.monotonic()
while time.monotonic() - start < 60 and not self_future.done():
    for server_name in config["servers"]:
        try:
            if requests.get(f"http://{server_name}:9999/server_id").json() == server_id:
                print("It's me!")
                self_future.set_result(server_name)
                break
        except requests.RequestException as exc:
            time.sleep(1)
            continue

app_done.result()
