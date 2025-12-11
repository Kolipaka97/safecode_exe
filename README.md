Secure Python Code Runner API 

A simple API where users can submit Python code and see the output.
The code runs inside Docker containers 

Features
- Run Python code safely inside Docker (python:3.11-slim).
- One endpoint: POST /run.
- Resource limits:
- Timeout: 10 seconds
- No network access
- Read-only filesystem
- Code length restriction: max 5000 characters 
- Clear error messages (Execution timed out after 10 seconds).

Prerequisites
- Python 3.11+
- Docker installed and running
- Flask & Flask-CORS

Install dependencies

pip install flask flask-cors
python app.py
http://localhost:5000

PI Usage

Endpoint
POST /run
Request Body

Download Thunder client 
python -m pip install flask-cors
python -m http.server 5500
http://127.0.0.1:5500/index.html
Go to this ip

or

json Entre the test code click on send will get the test results

 Security Measures
- Timeout (10s) → prevents infinite loops.
- Memory limit (128 MB) → stops memory bombs.
- CPU limit (1 core) → prevents resource hogging.
- No network access → blocks malicious requests.
- Read-only filesystem → prevents file writes.
- Code length restriction (≤ 5000 chars) → avoids oversized submissions.

Docker Security Experiments
> Infinite Loop
while True:
    pass


Returns: "Execution timed out after 10 seconds"
> Memory Bomb
x = "a" * 1000000000


 Killed safely, no crash.
> Network Access
import requests
requests.get("http://evil.com")


 Blocked: "Network is unreachable"
> File Access
with open("/etc/passwd") as f:
    print(f.read())


 What I Learned
- Docker provides process isolation, but not complete security.
- How to Execute Untrusted Code Safely
- Mounted volumes expose host files — be careful what you mount.
- CPU limits prevent infinite loops
- Memory limits prevent crashes












