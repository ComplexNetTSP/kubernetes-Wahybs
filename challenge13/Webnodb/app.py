from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>My Flask App</title>
        </head>
        <body>
            <h1>Aziz ZRIBI</h1>
            <h2>Nom Projet: NET 4255 serveur flask</h2>
            <h3>Version: V2</h3>
            <h4>Server Hostname: {request.url}</h4>
            <h5>Current Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</h5>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
