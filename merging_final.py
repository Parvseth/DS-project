import pandas as pd
import glob

# Path to the folder containing the Excel files
file_path = r"C:\Code_data\DS project\all aggregates\*.xlsx"

# List to hold each file's data
dataframes = []

# Load each file and append it to the list
for file in glob.glob(file_path):
    df = pd.read_excel(file)
    dataframes.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
combined_data = pd.concat(dataframes, ignore_index=True)

# Save the combined data to a new Excel file
combined_data.to_excel(r"C:\Code_data\DS project\combined_data.xlsx", index=False)

print("All files have been combined into combined_data.xlsx")
