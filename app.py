
from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "V1")

@app.route("/")
def home():
    hostname = os.getenv("HOSTNAME", "unknown")

    return f"""
    <html>
    <head>
        <title>Jenkins DevSecOps Lab</title>
    </head>
    <body style="font-family: Arial; text-align: center; padding-top: 80px;">
        <h1>JENKINS DEVSECOPS LAB</h1>
        <h2>Kubernetes Rolling Update</h2>
        <hr>
        <h1>APPLICATION VERSION: {VERSION}</h1>
        <h3>Pod: {hostname}</h3>
        <p>Application Status: RUNNING</p>
        <hr>
        <p>Built and deployed through Jenkins.</p>
    </body>
    </html>
    """

app.run(host="0.0.0.0", port=5000)
EOF
