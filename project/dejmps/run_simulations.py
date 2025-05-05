import subprocess
import os
import numpy as np
import yaml

def update_all_link_fidelities(yaml_path, new_fidelity):
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    for link in data.get("links", []):
        link["fidelity"] = new_fidelity

    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, sort_keys=False)

def update_all_nodes_gate_fidelity(yaml_path, new_gate_fidelity):
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    for node in data.get("nodes", []):
        node["gate_fidelity"] = new_gate_fidelity

    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, sort_keys=False)


def run_netqasm_simulate(n_max, n_succ):
    """
    Runs the 'netqasm simulate' command multiple times.

    :param n_times: The number of times to run the simulation.
    """

    fidelities_to_run = np.arange(0.5,1.05,0.05)

    titles = np.char.mod('%.2f', fidelities_to_run)
    titles = np.char.replace(titles, ".", "")
    #
    for arg in range(len(fidelities_to_run)):
        #Run for specific fidelity
        fid = fidelities_to_run[arg]

        if fid > 1.0:
            fid = 1.0

        update_all_link_fidelities("network.yaml", float(fid))


        #Create a unique file name to store the data
        title_fid = titles[arg]
        filename = f"dejmps_depol_{title_fid}.txt"
        results_file_path = os.path.join("data", filename)

        # Create and initialize the file
        with open(results_file_path, "w") as f:
            f.write("")  # Ensure the file exists

        with open("filename.txt", "w") as f:
            f.write(filename)

        results_file_path = os.path.join("data", filename)
        # Write the result to a text file
        with open(results_file_path, "a") as f:
            f.write(f"{fid}\n")
            # f.write("1.0\n")

        i = 0
        while i < n_max:
            print(f"Running simulation iteration {i + 1}...")

            #Determine number of succesfull entanglement generations, if n_succ: break
            results = np.loadtxt(results_file_path)
            results = np.atleast_1d(results)
            length = len(results)-1

            if length == n_succ:
                with open(results_file_path, "a") as f:
                    f.write(f"{i+1}\n")
                break

            # Run the 'netqasm simulate' command
            result = subprocess.run(["netqasm", "simulate"], capture_output=True, text=True)

            # Check if the simulation was successful
            if result.returncode == 0:
                # print(f"Iteration {i + 1} completed successfully.")
                print(result.stdout)  # Output of the simulation
            else:
                print(f"Iteration {i + 1} failed with error:")
                print(result.stderr)  # Error message if it fails

            i += 1


if __name__ == "__main__":
    n_max = 300 # Change to how many times you want to run the simulation
    n_succ = 50
    run_netqasm_simulate(n_max, n_succ)

