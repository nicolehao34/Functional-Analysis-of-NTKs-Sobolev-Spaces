from torch.utils.data import TensorDataset, DataLoader
import torch
import torch.nn as nn


def train_fno(model, inputs, targets, epochs=100, batch_size=20, lr=1e-3):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.MSELoss()

    dataset = TensorDataset(torch.tensor(inputs, dtype=torch.float32), 
                            torch.tensor(targets, dtype=torch.float32))
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    for epoch in range(epochs):
        for x_batch, y_batch in loader:
            x_batch, y_batch = x_batch.to(device), y_batch.to(device)
            out = model(x_batch)
            loss = loss_fn(out, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch}: Loss = {loss.item():.4e}")
