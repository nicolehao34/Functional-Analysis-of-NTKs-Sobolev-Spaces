import numpy as np
from model import burgers_spectral_solver

def generate_dataset(num_samples=1000, N=1024):
    inputs, outputs = [], []
    for _ in range(num_samples):
        _, u0, uT = burgers_spectral_solver(N=N)
        inputs.append(u0)
        outputs.append(uT)
    return np.array(inputs), np.array(outputs)
