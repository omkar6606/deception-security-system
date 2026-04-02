from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

def log_alert(ip, action):
    with open("alerts.log", "a") as f:
        f.write(f"{datetime.datetime.now()} | {ip} | {action}\n")

login_page = """
<h2>Admin Login</h2>
<form method="POST">
  Username: <input name="username"><br>
  Password: <input name="password" type="password"><br>
  <input type="submit">
</form>
"""

@app.route("/", methods=["GET", "POST"])
def fake_login():
    if request.method == "POST":
        ip = request.remote_addr
        username = request.form.get("username")

        print("🚨 ALERT: Fake login triggered!")
        log_alert(ip, f"Fake Login Attempt: {username}")

        return "Access Denied!"

    return render_template_string(login_page)

if __name__ == "__main__":
    app.run(port=5000)