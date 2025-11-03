import os 
from tqdm import tqdm
path = 'images/'
files = os.listdir(path)


for i, file in enumerate(tqdm(files)):
    old_path = os.path.join(path, file)
    old_name = file
    old_format = file.split('.')[-1]
    new_path = os.path.join(path, f"{i}.{old_format}")
    os.rename(old_path, new_path)


