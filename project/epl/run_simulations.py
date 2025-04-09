import subprocess
import time
from datetime import datetime
import os

def run_netqasm_simulate(n_times):
    """
    Runs the 'netqasm simulate' command multiple times.

    :param n_times: The number of times to run the simulation.
    """

    # Create a unique HDF5 file name using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data_{timestamp}.txt"
    results_file_path = os.path.join("data", filename)

    # Create and initialize the file
    with open(results_file_path, "w") as f:
        f.write("")  # Ensure the file exists

    with open("filename.txt", "w") as f:
        f.write(filename)

    for i in range(n_times):
        print(f"Running simulation iteration {i + 1}...")

        # Run the 'netqasm simulate' command
        result = subprocess.run(["netqasm", "simulate"], capture_output=True, text=True)

        # Check if the simulation was successful
        if result.returncode == 0:
            # print(f"Iteration {i + 1} completed successfully.")
            print(result.stdout)  # Output of the simulation
        else:
            print(f"Iteration {i + 1} failed with error:")
            print(result.stderr)  # Error message if it fails

        # Optionally, add a delay between simulations if needed
        time.sleep(1)


if __name__ == "__main__":
    n_times = 5  # Change to how many times you want to run the simulation
    run_netqasm_simulate(n_times)

