from datetime import datetime

def get_current_time():
    """Returns the current time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_ping_spike(log_file, name, previous_ping, current_ping):
    """Logs a detected ping spike to the file."""
    log_entry = (
        f"[{get_current_time()}] [{name}] Spike detected! "
        f"Previous: {previous_ping} ms, Current: {current_ping} ms\n"
    )
    log_file.write(log_entry)
    log_file.flush()


def log_no_spike(log_file):
    """Logs when no ping spike is detected."""
    log_entry = f"[{get_current_time()}] No spike detected.\n"
    log_file.write(log_entry)
    log_file.flush()
