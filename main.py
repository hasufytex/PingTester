from ping_utils import ping_target
from logger import log_ping_spike, log_no_spike, get_current_time
from display import display_results_in_table
import time
from datetime import datetime

# Settings
TARGETS = {
    "localhost": "localhost",
    "Cloudflare": "1.1.1.1",
    "Google": "8.8.8.8",
}
INTERVAL = 1  # Ping interval in seconds
SPIKE_THRESHOLD = 10  # Spike threshold in ms
OUTPUT_FILE = "ping_spikes.log"

def detect_ping_spikes():
    """Detects ping spikes across multiple targets and logs them."""
    last_ping_times = {name: None for name in TARGETS}
    with open(OUTPUT_FILE, "a") as log_file:
        log_file.write(f"Started ping test at {get_current_time()}\n")

        while True:
            spikes_detected = False
            results = []

            for name, target in TARGETS.items():
                ping_time = ping_target(target)
                spike = ""
                delta = ""
                status = ""

                if ping_time is not None:
                    if last_ping_times[name] is not None:
                        delta = abs(ping_time - last_ping_times[name])  # Calculate the delta
                        if delta > SPIKE_THRESHOLD:
                            spike = "Spike!"
                            status = f"Spike! ({delta} ms)"
                            spikes_detected = True
                        else:
                            status = f"Stable"
                    else:
                        status = "Stable (Initial)"
                    
                    last_ping_times[name] = ping_time
                else:
                    ping_time = "Timeout"
                    delta = "N/A"
                    status = "Timeout"

                results.append([name, ping_time, delta, status])

            display_results_in_table(results)

            if not spikes_detected:
                log_no_spike(log_file)

            time.sleep(INTERVAL)

if __name__ == "__main__":
    detect_ping_spikes()
