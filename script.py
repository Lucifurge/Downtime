from concurrent.futures import ThreadPoolExecutor
import random
import string
import time
import requests

class CMEModule:
    name = 'fakesim'
    description = 'Fake virus simulator + web POST sender'
    supported_protocols = ['smb']
    opsec_safe = True
    multiple_hosts = True

    def __init__(self, context, options):
        self.context = context
        self.options = options

        # Parse options from CME command line
        self.target_url = self.options.get('URL')
        self.requests_to_send = int(self.options.get('NUM', 20))
        self.max_workers = int(self.options.get('THREADS', 5))
        self.visible_logs = int(self.options.get('LOGS', 10))

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
        print(f"[SIMULATION] Writing fake payload to {file_path} (NOT ACTUALLY WRITTEN)")

    def scan_and_infect(self):
        fake_files = [f"file_{i}.txt" for i in range(5)]
        for f in fake_files:
            self.infect_file(f)
            time.sleep(0.1)

    def connect_to_command_center(self):
        print("[SIMULATION] Connecting to attacker server... (no real connection)")

    def run(self):
        print("[SIMULATION] Fake Virus Simulation Started.")
        self.connect_to_command_center()
        self.scan_and_infect()
        print("[SIMULATION] Simulation finished.")

        print(f"\n🚀 Sending {self.requests_to_send} requests to {self.target_url} (only showing first {self.visible_logs})...")
        start = time.time()

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for i in range(self.requests_to_send):
                executor.submit(self.send_post, i)

        duration = round(time.time() - start, 2)
        print(f"\n✅ Done sending {self.requests_to_send} requests in {duration} seconds.")
