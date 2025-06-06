import torch
import torch.nn as nn
import torch.fft

class SpectralConv1d(nn.Module):
    def __init__(self, in_channels, out_channels, modes):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.modes = modes
        self.weights = nn.Parameter(torch.randn(in_channels, out_channels, modes, dtype=torch.cfloat))

    def forward(self, x):
        x_ft = torch.fft.rfft(x, dim=-1)
        out_ft = torch.zeros_like(x_ft, dtype=torch.cfloat)
        out_ft[..., :self.modes] = torch.einsum("bci,cio->bco", x_ft[..., :self.modes], self.weights)
        x = torch.fft.irfft(out_ft, n=x.size(-1), dim=-1)
        return x

class FNO1D(nn.Module):
    def __init__(self, modes, width):
        super().__init__()
        self.fc0 = nn.Linear(1, width)
        self.conv1 = SpectralConv1d(width, width, modes)
        self.conv2 = SpectralConv1d(width, width, modes)
        self.fc1 = nn.Linear(width, 128)
        self.fc2 = nn.Linear(128, 1)

    def forward(self, x):
        x = x.unsqueeze(-1)
        x = self.fc0(x)
        x = self.conv1(x) + x
        x = self.conv2(x) + x
        x = self.fc1(x)
        return self.fc2(x).squeeze(-1)

        return self.fc2(x).squeeze(-1)
