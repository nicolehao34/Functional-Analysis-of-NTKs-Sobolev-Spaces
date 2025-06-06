from data import generate_dataset
from model import FNO1D
from train import train_fno
from sobolev import H1_norm
import numpy as np
import torch

# Generate data
inputs, targets = generate_dataset(num_samples=1000, N=1024)
dx = 2 * np.pi / 1024

# Train FNO
model = FNO1D(modes=16, width=64)
train_fno(model, inputs, targets, epochs=100)

# Evaluate H1 Error
pred = model(torch.tensor(inputs, dtype=torch.float32)).detach().numpy()
h1_errors = [H1_norm(p - t, dx) for p, t in zip(pred, targets)]
print(f"Average H1 Error: {np.mean(h1_errors):.4e}")