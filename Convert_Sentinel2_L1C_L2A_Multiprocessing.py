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
import time
from tqdm import tqdm

sen2cor_path = r"C:\Users\****\.snap\auxdata\Sen2Cor-02.11.00-win64\L2A_Process.bat"
input_folder = r"J:\Prefire_GS\safe_folders"
output_folder = r"J:\Prefire_GS\L2A"

NUM_CORES = 4 # Set the number of logical processors you want to utilise

os.makedirs(output_folder, exist_ok=True)
def process_sentinel2_l1c(file_path):
    start_time = time.time()
    cmd = [sen2cor_path, "--output_dir", output_folder, file_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if result.returncode != 0:
        return f"ERROR: {file_path} failed! ({elapsed_time:.2f} sec)\n{result.stderr}"
    else:
        return f"SUCCESS: {file_path} processed in {elapsed_time:.2f} sec!"
safe_folders = [os.path.join(input_folder, folder) for folder in os.listdir(input_folder)
                if os.path.isdir(os.path.join(input_folder, folder)) and folder.endswith(".SAFE")]

print(f"Using {NUM_CORES} CPU cores to process {len(safe_folders)} Sentinel-2 images...\n")

if safe_folders:
    print("Estimating processing time...")
    start_sample_time = time.time()
    process_sentinel2_l1c(safe_folders[0])
    sample_time = time.time() - start_sample_time
    est_time_per_image = sample_time
    est_total_time = (len(safe_folders) / NUM_CORES) * est_time_per_image
    print(f"Estimated total time: {est_total_time / 60:.2f} minutes ({est_total_time:.2f} sec)\n")
start_time_total = time.time()
with multiprocessing.Pool(processes=NUM_CORES) as pool:
    results = list(tqdm(pool.imap(process_sentinel2_l1c, safe_folders), total=len(safe_folders)))
for res in results:
    print(res)
end_time_total = time.time()
actual_time_taken = end_time_total - start_time_total

print(f"\nAll images processed successfully in {actual_time_taken / 60:.2f} minutes ({actual_time_taken:.2f} sec)!\n")
