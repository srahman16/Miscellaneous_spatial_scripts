'''
Title: Batch process Sentinel-2 (L1C) to Sentinel-2 (L2A) Product (with visualising Estimated Processing Time)
Author: Shahriar Rahman
Version: 3
Date: 17 March 2025
E-mail: shahriar.env12@gmail.com
'''
import subprocess
import os
import multiprocessing
from tqdm import tqdm

sen2cor_path = r"C:\Users\SmartSat\.snap\auxdata\Sen2Cor-02.11.00-win64\L2A_Process.bat"
input_folder = r"J:\Prefire_GS\safe_folders"
output_folder = r"J:\Prefire_GS\L2A"

NUM_CORES = 60

os.makedirs(output_folder, exist_ok=True)

# Function to process an L1C image
def process_sentinel2_l1c(file_path):
    cmd = [sen2cor_path, "--output_dir", output_folder, file_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    return f"SUCCESS: {file_path}" if result.returncode == 0 else f"ERROR: {file_path} failed!"

if __name__ == '__main__':
    # Get all .SAFE folders
    safe_folders = [os.path.join(input_folder, folder) for folder in os.listdir(input_folder)
                    if os.path.isdir(os.path.join(input_folder, folder)) and folder.endswith(".SAFE")]
    print(f"Using {NUM_CORES} CPU cores to process {len(safe_folders)} Sentinel-2 images...")
    with multiprocessing.Pool(processes=NUM_CORES) as pool:
        results = list(tqdm(pool.imap(process_sentinel2_l1c, safe_folders), total=len(safe_folders)))
    for res in results:
        print(res)
    print("All images processed successfully!")


## 100%|██████████| 104/104 [1:29:17<00:00, 51.51s/it]# Progress Bar
