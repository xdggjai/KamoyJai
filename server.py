from flask import Flask, request
from threading import Thread

app = Flask(__name__)

@app.route('/')##methods=['POST']
def receive_command():
    data = request.json
    print(f"Received: {data}")
    return {"status": "success"}, 200

def run():
    app.run(host="0.0.0.0", port=8080)

def server_on():
    t = Thread(target=run)
    t.start()