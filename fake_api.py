from flask import Flask, request
import datetime

app = Flask(__name__)

def log_alert(ip, endpoint):
    with open("alerts.log", "a") as f:
        f.write(f"{datetime.datetime.now()} | {ip} | Accessed {endpoint}\n")

@app.route("/internal-api", methods=["GET", "POST"])
def fake_api():
    ip = request.remote_addr

    print("🚨 ALERT: Fake API accessed!")
    log_alert(ip, "/internal-api")

    return {"message": "Unauthorized access detected"}, 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)