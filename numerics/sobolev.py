# H^norm error calculation

import numpy as np

def H1_norm(u, dx):
    u = np.array(u)
    du_dx = np.gradient(u, dx)
    return np.sqrt(np.sum(u**2) * dx + np.sum(du_dx**2) * dx)

