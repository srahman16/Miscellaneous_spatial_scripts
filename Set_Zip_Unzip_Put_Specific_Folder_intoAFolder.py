'''
Title: Set .zip extension, unzip all in one folder, then take specific folder (with contents) into a separate folder (here: .SAFE)
Sub-Title: This is how we can zip up the Sentinel-1 (L1C) files, and then put all the .SAFE folders into a specific folder
Author: Shahriar Rahman
E-mail: shahriar.env12@gmail.com
Version: 5
Date: 17 March 2025
'''

import os
import zipfile
import shutil

source_folder = r"J:\Prefire_GS" # Where all the files without .zip extension
extract_folder = r"J:\Prefire_GS\unzipped" # Unzipped folders
safe_output_folder = r"J:\Prefire_GS\safe_folders" # Location where all the .SAFE folder will be placed

os.makedirs(extract_folder, exist_ok=True)
os.makedirs(safe_output_folder, exist_ok=True)

## Functions

def rename_files_to_zip(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and not filename.endswith(".zip"):
            new_file_path = file_path + ".zip"
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} ➝ {filename}.zip")


def unzip_files(directory, output_dir):
    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            zip_path = os.path.join(directory, filename)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                extract_to = os.path.join(output_dir, os.path.splitext(filename)[0])
                zip_ref.extractall(extract_to)
                print(f"Extracted: {filename} to {extract_to}")

def move_safe_folders(extracted_dir, safe_output_dir):
    for root, dirs, files in os.walk(extracted_dir): 
        for folder in dirs:
            if folder.endswith(".SAFE"): 
                safe_folder_path = os.path.join(root, folder)  
                new_location = os.path.join(safe_output_dir, folder)
                if not os.path.exists(new_location):
                    shutil.move(safe_folder_path, new_location)
                    print(f"Moved: {safe_folder_path} ➝ {new_location}")
                else:
                    print(f"Skipped (Already Exists): {folder}")
        break

rename_files_to_zip(source_folder)
unzip_files(source_folder, extract_folder)
move_safe_folders(extract_folder, safe_output_folder)

print("All .SAFE folders are now moved successfully!")
