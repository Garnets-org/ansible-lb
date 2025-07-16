from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": f"Hello from {socket.gethostname()}",
        "available_servers": ["app1", "app2", "app3", "app4", "app5"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

