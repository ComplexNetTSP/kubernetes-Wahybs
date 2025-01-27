from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://mongodb:27017/")  
db = client.net4255  
collection = db.requests  

@app.route("/")
def home():
    # Enregistrer IP du client
    client_ip = request.remote_addr
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #Inserer  IP et le temps dans la collection
    collection.insert_one({"ip": client_ip, "date": current_time})
    # Trouver les 10 dernieres enregistrements dans la DB
    last_records = collection.find().sort("_id", -1).limit(10)

    records_html = "<ul>"
    for record in last_records:
        records_html += f"<li>IP: {record['ip']}, Date: {record['date']}</li>"
    records_html += "</ul>"


    return f"""
    <html>
        <head>
            <title>My Flask App</title>
        </head>
        <body>
            <h1>Aziz ZRIBI</h1>
            <h2>Nom Projet: NET 4255 serveur flask</h2>
            <h3>Version: V1</h3>
            <h4>Server Hostname: {request.url}</h4>
            <h5>Current Date: {current_time}</h5>
            <h6>Last 10 Requests:</h6>
            {records_html}
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
