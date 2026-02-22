import time
from typing import Dict, List

class HealthChecker:
    def __init__(self):
        self.checks = {}

    def register_check(self, name, check_fn, timeout=5):
        pass

    def run_check(self, name) -> Dict:
        # Return: {'name': name, 'status': 'healthy'/'unhealthy', 'response_time_ms': N, 'error': None}
        pass

    def run_all(self) -> Dict:
        # overall = 'healthy' if all pass, 'degraded' if some fail, 'unhealthy' if all fail
        # Return: {'status': overall, 'checks': [...], 'timestamp': ISO}
        pass


# Simulated dependency checks
def check_database():
    time.sleep(0.01)  # Simulate 10ms latency
    return True

def check_cache():
    time.sleep(0.005)
    return True

def check_external_api():
    raise ConnectionError("API unreachable")  # Simulates failure
