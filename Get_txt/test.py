from tqdm import tqdm
import time

for task in tqdm(range(100), leave=True):
    print('\n')
    time.sleep(0.1)
