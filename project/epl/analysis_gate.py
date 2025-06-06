import numpy as np
import os
import matplotlib.pyplot as plt

def open_files():
    folder_path = "./data"  # Folder path
    files = [f for f in os.listdir(folder_path) if "gate" in f]
    full_paths = [os.path.join(folder_path, f) for f in files]
    return full_paths

def analyse(files):
    data = np.array([np.loadtxt(path) for path in files])

    gate_fidelity = data[:,0]
    results = data[:, 1:-1]
    num_runs = data[:, -1]

    arg_sort = np.argsort(gate_fidelity)
    gate_fidelity = gate_fidelity[arg_sort][::2]
    results = results[arg_sort][::2]
    num_runs = num_runs[arg_sort]

    mean_meas_fids = np.mean(results,axis=1)


    plt.plot(gate_fidelity, mean_meas_fids,".")
    plt.grid()
    plt.xlabel(r'F$_\mathrm{gate}$')
    plt.ylabel(r"$\bar{\mathrm{F}}_\mathrm{dist}$")
    plt.savefig("figures/avg_fidelity_gate_sweep_50_successes.png", dpi=500)


if __name__ == "__main__" :
    files = open_files()
    analyse(files)

