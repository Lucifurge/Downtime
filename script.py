import time
import random
import string
import argparse
from concurrent.futures import ThreadPoolExecutor
import requests

# -----------------------
# User Agents
# -----------------------
user_agents = [
    "Mozilla/5.0 (Linux; Android 12)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)",
]

payload = {
    "username": "test_user",
    "password": "123456",
    "data": "HelloWorld"
}

# -----------------------
# Web request sender
# -----------------------
def send_post(i, target_url, visible_logs):
    try:
        headers = {
            "User-Agent": random.choice(user_agents),
            "Content-Type": "application/json"
        }
        response = requests.post(target_url, json=payload, headers=headers, timeout=3)
        if i < visible_logs:
            print(f"[{i+1}] ✅ Status: {response.status_code}")
    except requests.RequestException:
        if i < visible_logs:
            print(f"[{i+1}] ❌ Request failed")

# -----------------------
# Fake virus-like (educational only)
# -----------------------
def generate_payload():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=50))

def infect_file(file_path):
    print(f"Infecting file: {file_path}")
    payload = generate_payload()
    print(f"Payload (not written): {payload[:10]}...")

def scan_and_infect():
    fake_files = [f"file_{i}.txt" for i in range(3)]
    for f in fake_files:
        infect_file(f)
        time.sleep(0.2)

def connect_to_command_center():
    print("Connecting to fake server... (no real connection)")

# -----------------------
# Main runner
# -----------------------
def main():
    parser = argparse.ArgumentParser(description="Request Sender Tool (Termux friendly)")
    parser.add_argument("-u", "--url", type=str, required=True, help="Target URL (ex: http://127.0.0.1:5000/)")
    parser.add_argument("-n", "--num", type=int, default=20, help="Number of requests to send")
    parser.add_argument("-t", "--threads", type=int, default=5, help="Number of concurrent threads")
    parser.add_argument("-l", "--logs", type=int, default=10, help="How many results to log visibly")
    args = parser.parse_args()

    print("⚡ Fake Virus Simulation Started ⚡")
    connect_to_command_center()
    scan_and_infect()
    print("Simulation finished.")

    print(f"\n🚀 Sending {args.num} requests to {args.url} (showing first {args.logs})...")  
    start = time.time()  

    with ThreadPoolExecutor(max_workers=args.threads) as executor:  
        for i in range(args.num):  
            executor.submit(send_post, i, args.url, args.logs)  

    duration = round(time.time() - start, 2)  
    print(f"\n✅ Done sending {args.num} requests in {duration} seconds.")

if __name__ == "__main__":
    main()        headers = {
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
