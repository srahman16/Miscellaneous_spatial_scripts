'''Sorting (ascending) list of files based on a date part embedded in the name
	and print it in a text (.txt) document'''
	
# Script: Shahriar Rahman
# Email: shahriar.env12@gmail.com
# Application: can be applied to sort any types of files in a given directory based on a date/part of the filenames
import os
from datetime import datetime

# Replace with the actual folder path
folder_path = r"A:\.....\..." 

# Replace with the desired output file name
output_file = r"A:\.....\XYZ.txt"  

# Get all .tiff files in the folder [you can set the file extension you are dealing with (e.g., .img, .shp)]
files = [f for f in os.listdir(folder_path) if f.endswith(".tif")]

# Extract the date part and create a list of tuples

file_dates = []

for file in files:
	# Assumes the date part is always the fourth element after splitting by "_"
    date_str = file.split("_")[3]  
    date = datetime.strptime(date_str, "%d%b%Y")
    file_dates.append((file, date))

# Sort the file_dates list based on the date in ascending order
sorted_files = sorted(file_dates, key=lambda x: x[1])

# Write the sorted filenames to the output file
with open(output_file, "w") as f:
    for file, _ in sorted_files:
        f.write(file + "\n")

print("Files are sort and the generated text document is here", output_file)