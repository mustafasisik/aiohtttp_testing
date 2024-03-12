import multiprocessing
import subprocess
from sys import  argv


def run_code(process_index):
    # Replace 'your_script.py' with the filename of your Python script
    subprocess.run(["python", "client_throughput.py", argv[2]])


if __name__ == "__main__":
    # Define the number of times you want to run the code
    num_processes = int(argv[1])

    # Create a pool of processes to run the code in parallel
    with multiprocessing.Pool(processes=num_processes) as pool:
        pool.map(run_code, range(num_processes))
