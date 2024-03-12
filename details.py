import psutil
import time
import logging


# Function to monitor CPU and memory usage
def monitor_resources():
    while True:
        # Get CPU usage percentage
        cpu_percent = psutil.cpu_percent(interval=1)
        # Get memory usage statistics
        memory_percent = psutil.virtual_memory().percent
        print(f"CPU Usage:{cpu_percent}%, Memory: {memory_percent}%")
        time.sleep(1)

if __name__ == "__main__":
    monitor_resources()
