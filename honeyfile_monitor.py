import os
import time
import datetime

FILE = "secret_admin_passwords.txt"

def log_alert(message):
    with open("alerts.log", "a") as f:
        f.write(f"{datetime.datetime.now()} | {message}\n")

# Get initial access time
last_access = os.stat(FILE).st_atime

print("🟢 Monitoring honeyfile...")

while True:
    current_access = os.stat(FILE).st_atime

    if current_access != last_access:
        print("🚨 ALERT: Honeyfile accessed!")
        log_alert("Honeyfile accessed")

        last_access = current_access

    time.sleep(2)