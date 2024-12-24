# src/data/data_loader.py
import torch
from torchvision import datasets, transforms # type: ignore
from torch.utils.data import DataLoader

def get_data_loaders(batch_size=32):
    # Define transformations
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    # Load Fashion-MNIST
    train_dataset = datasets.FashionMNIST('data/raw', 
                                         train=True, 
                                         download=True, 
                                         transform=transform)
    
    test_dataset = datasets.FashionMNIST('data/raw', 
                                        train=False, 
                                        download=True, 
                                        transform=transform)
    
    # Create data loaders
    train_loader = DataLoader(train_dataset, 
                            batch_size=batch_size, 
                            shuffle=True)
    
    test_loader = DataLoader(test_dataset, 
                           batch_size=batch_size, 
                           shuffle=False)
    
    return train_loader, test_loader