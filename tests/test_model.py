# tests/test_model.py
import torch
from src.models.cnn_model import FashionCNN # type: ignore

def test_model_output():
    model = FashionCNN()
    input_tensor = torch.randn(1, 1, 224, 224)
    output = model(input_tensor)
    assert output.shape == (1, 10)

def test_model_training():
    model = FashionCNN()
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters())
    
    # Mock data
    inputs = torch.randn(4, 1, 224, 224)
    labels = torch.randint(0, 10, (4,))
    
    # Forward pass
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    assert True  # If we get here, training step worked