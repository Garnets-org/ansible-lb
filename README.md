
# Flask Load Balancer Project (Ansible + NGINX + Docker)
This project sets up a dynamic, containerized Flask application environment behind an NGINX Load Balancer, fully automated via Ansible. Each Flask container reports its own status and peers via a styled web interface, enabling fault visibility and round-robin request distribution.

## Challenge Requirements Fulfilled
Requirement	Status
Load Balancer on VM, configured using Ansible only	✅
Round-robin algorithm via NGINX	✅
5 Flask upstream servers, containerized	✅
Flask apps detect and display request origin + online peers	✅
All files stored in version-controlled public repo	✅

 ## Structure
Ubuntu VM  (Load Balancer)
│
├── Ansible playbook installs NGINX
├── NGINX reverse proxy config (round-robin to 5 apps)
│
└── Targets Red Hat VM running:
     ├── Docker Compose
     ├── 5 Flask containers (ports 6001–6005)
     └── Dynamic peer health-check logic inside each app
## Flask App Behavior
Each containerized app:

Displays its hostname, container IP, and timestamp

Uses an environment variable ALL_SERVERS to detect all expected peers

Queries /health endpoint of each peer

UI shows:

✅ Online peers

🔴 Offline peers

🔁 Auto-refresh every 10s

🌓 Toggleable dark/light theme

📦 Project Folder Structure

##Folder Structure.
├── ansible-playbook.yaml         # Ansible entry file
├── inventory.ini                 # Load balancer host config
├── roles/loadbalancer/          # Ansible role for NGINX setup
│   ├── tasks/main.yaml
│   └── handlers/main.yaml
│
├── flask-lb-demo/
│   ├── docker-compose.yaml       # Deploys all 5 Flask containers
│   └── upstream-apps/
│       ├── app.py                # Flask logic with peer health check
│       └── templates/index.html  # UI with toggle theme and status logic
##Sample Output
Top of the page:
Taye’s Flask Load Balancer
✅ All servers are online
Container Info Section:
Hello from: app1
This server is online and responding to traffic.
Container IP Address: 172.18.0.4
Timestamp: 2025-07-17 13:45:00
Server List Section

## 
🟢 Online Servers
  - app1
  - app2
  - app3
  - app4
  - app5

🔘 All Registered Servers
  - 🟢 app1
  - 🟢 app2
  - 🟢 app3
  - 🟢 app4
  - 🟢 app5
## How to Use
```bash 
1. On Load Balancer VM (Ubuntu)
ansible-playbook -i inventory.ini ansible-playbook.yaml
2. On Upstream Server VM (Red Hat)
cd flask-lb-demo/
docker compose up --build -d
3. Access via Browser
Open your Load Balancer VM’s public IP

Refresh to see different upstream containers respond (round-robin)

## Tech Stack
Ansible – Automation for LB setup

NGINX – Round-robin reverse proxy

Flask – Minimal Python app

Docker Compose – 5 containerized app instances

Jinja2 + HTML + JS – Templating + live theme switch + auto-refresh

## Notes
If any container is stopped manually (e.g., docker stop app2), the web UI reflects it within 10 seconds.

ALL_SERVERS is passed as an environment variable during Docker Compose to enable peer scanning.

The project emphasizes real-world fault visibility and dynamic service awareness.

## Author
Taye Akin
DevOps & Cloud Enthusiast

