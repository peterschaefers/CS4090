import numpy as np
import os
import matplotlib.pyplot as plt

def open_files(folder_path, noise_type):
    files = [f for f in os.listdir(folder_path) if noise_type in f]
    full_paths = [os.path.join(folder_path, f) for f in files]
    return full_paths

def analyse():
    path_321 = '../three_to_one/data'
    path_dejmps = '../dejmps/data'
    path_epl = '../epl/data'

    files_depol_321 = open_files(path_321, 'depol')
    files_depol_dejmps = open_files(path_dejmps, 'depol')
    files_depol_epl = open_files(path_epl, 'depol')

    files_gate_321 = open_files(path_321, 'gate')
    files_gate_dejmps = open_files(path_dejmps, 'gate')
    files_gate_epl = open_files(path_epl, 'gate')

    data_depol_321 = np.array([np.loadtxt(path) for path in files_depol_321])
    data_depol_dejmps = np.array([np.loadtxt(path) for path in files_depol_dejmps])
    data_depol_epl = np.array([np.loadtxt(path) for path in files_depol_epl])

    data_gate_321 = np.array([np.loadtxt(path) for path in files_gate_321])
    data_gate_dejmps = np.array([np.loadtxt(path) for path in files_gate_dejmps])
    data_gate_epl = np.array([np.loadtxt(path) for path in files_gate_epl])

    fidelity_depol_321 = data_depol_321[:,0]
    res_fidelity_depol_321 = data_depol_321[:,1:-1]
    num_runs_depol_321 = data_depol_321[:,-1]

    arg_sort = np.argsort(fidelity_depol_321)

    fidelity_depol_321 = fidelity_depol_321[arg_sort]
    res_fidelity_depol_321 = res_fidelity_depol_321[arg_sort]
    num_runs_depol_321 = num_runs_depol_321[arg_sort]

    av_res_fidelity_depol_321 = np.mean(res_fidelity_depol_321,axis=1)


    plt.plot(fidelity_depol_321, av_res_fidelity_depol_321,c='blue')
    plt.grid()
    plt.xlabel(r'F$_\mathrm{depol}$')
    plt.ylabel(r"$\bar{\mathrm{F}}_\mathrm{dist}$")
    plt.savefig("figures/test.png")


if __name__ == "__main__" :
    analyse()

