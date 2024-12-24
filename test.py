import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

data_dir = os.getenv('DATA_DIR')
model_dir = os.getenv('MODEL_DIR')

# Use data_dir and model_dir to access files 
data_file = os.path.join(data_dir, 'train.csv') 
model_file = os.path.join(model_dir, 'my_model.pth') 

print(f"Data file path: {data_file}")
print(f"Model file path: {model_file}")