import numpy as np
from scipy.fft import fft, ifft

def burgers_spectral_solver(N=1024, T=1.0, dt=1e-3, nu=0.01):
    x = np.linspace(0, 2*np.pi, N, endpoint=False)
    k = np.fft.fftfreq(N, 1/N)
    k = 1j * k

    # Initial condition: smooth random Fourier series
    coeffs = np.random.randn(N) * np.exp(-0.5 * np.abs(k)**2)
    u0 = np.real(ifft(coeffs))
    u_hat = fft(u0)

    t = 0
    while t < T:
        u = np.real(ifft(u_hat))
        nonlinear = fft(u * u)
        u_hat = u_hat - dt * (0.5 * k * nonlinear + nu * (k**2) * u_hat)
        t += dt

    uT = np.real(ifft(u_hat))
    return x, u0, uT
