import subprocess
import platform
import re

def ping_windows(target):
    """Pings a target on Windows and returns the ping time."""
    result = subprocess.run(
        ["ping", "-n", "1", "-w", "1000", target],
        capture_output=True,
        text=True
    )
    return parse_ping_output(result.stdout)

def ping_unix(target):
    """Pings a target on Linux/macOS and returns the ping time."""
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", target],
        capture_output=True,
        text=True
    )
    return parse_ping_output(result.stdout)

def parse_ping_output(output):
    """Parses the ping output and extracts the ping time in ms."""
    # Updated regular expression to match both 'time=<value>ms' and 'time<value>ms'
    match = re.search(r'time[=<](\d+\.?\d*)ms', output)
    if match:
        return float(match.group(1))  # Return the ping time as float
    else:
        raise ValueError(f"Could not find a valid ping time in the output: {output}")

def ping_target(target):
    """Pings the given target and returns the ping time in milliseconds."""
    try:
        system_platform = platform.system().lower()

        if system_platform == "windows":
            return ping_windows(target)
        else:  # For Linux and macOS
            return ping_unix(target)
    
    except Exception as e:
        print(f"Error pinging {target}: {e}")
    return None

# Test the function
ping_target("8.8.8.8")  # For example, Google DNS
