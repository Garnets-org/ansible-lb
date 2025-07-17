from flask import Flask, render_template
import socket
import os
import requests
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    app_name = os.getenv("APP_NAME", "UnknownApp")
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Get all expected servers from environment variable
    servers_env = os.getenv("ALL_SERVERS", "")
    all_servers = servers_env.split(",") if servers_env else []

    # Check which are online
    online_servers = []
    for server in all_servers:
        try:
            res = requests.get(f"http://{server}/health", timeout=2)
            if res.status_code == 200:
                online_servers.append(server)
        except requests.exceptions.RequestException:
            continue

    return render_template(
        "index.html",
        hostname=hostname,
        app_name=app_name,
        ip=ip_address,
        timestamp=timestamp,
        all_servers=all_servers,
        online_servers=online_servers
    )

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

