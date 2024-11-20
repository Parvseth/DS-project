import os
import pandas as pd
import numpy as np

# Folder containing the CSV files
folder_path = r"E:\01-MFCC"  # Replace with the path to your folder

# Get all CSV filenames in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Step 1: Read the CSV files and store them in a list
mfcc_dataframes = []
for file_name in csv_files:
    file_path = os.path.join(folder_path, file_name)
    df = pd.read_csv(file_path, header=None)  # Assuming no header in your CSV files
    mfcc_dataframes.append(df)

# Step 2: Find the maximum number of columns across all dataframes
max_columns = max(df.shape[1] for df in mfcc_dataframes)

# Step 3: Pad each dataframe to the maximum number of columns
padded_mfccs = []
for df in mfcc_dataframes:
    # Pad with zeros to match the max_columns
    padded_array = np.pad(df.values, ((0, 0), (0, max_columns - df.shape[1])), 'constant')
    padded_mfccs.append(pd.DataFrame(padded_array))

# Step 4: Save the padded dataframes as new CSV files
output_folder = os.path.join(folder_path, "padded_csvs")  # Folder to save padded CSV files
os.makedirs(output_folder, exist_ok=True)

for i, padded_df in enumerate(padded_mfccs):
    output_filename = f"padded_mfcc_{i+1}.csv"  # Generate a new filename for each
    output_path = os.path.join(output_folder, output_filename)
    padded_df.to_csv(output_path, index=False, header=False)
    print(f"Saved {output_filename}")
