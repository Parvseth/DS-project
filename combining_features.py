import os
import pandas as pd

def load_and_save_aggregated_features(source_folder, output_filename, include_artist_label=False):
    """
    Load aggregated feature data from multiple Excel files in a folder, combine them,
    and save the combined dataset as a new Excel file.
    
    Parameters:
    - source_folder (str): Path to the folder containing Excel files.
    - output_filename (str): Filename for the combined Excel file to be saved.
    - include_artist_label (bool): If True, include the artist label (either manually entered or extracted from filename).
    
    Returns:
    - pd.DataFrame: Combined DataFrame with each row representing a song and columns as aggregated features.
    """
    # List all Excel files in the specified folder
    excel_files = [f for f in os.listdir(source_folder) if f.endswith('.xlsx')]
    
    # Initialize an empty list to store DataFrames
    dataframes = []
    
    # Prompt for artist name once
    if include_artist_label:
        artist_label = input("Enter the artist name to apply to all files: ")
    
    for file in excel_files:
        # Load each Excel file into a DataFrame
        file_path = os.path.join(source_folder, file)
        df = pd.read_excel(file_path, header=None)
        
        # Add artist label to the DataFrame (apply the same artist name for all files)
        if include_artist_label:
            df['artist'] = artist_label
        
        # Append the DataFrame to the list
        dataframes.append(df)
    
    # Combine all DataFrames into a single DataFrame
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    # Save the combined DataFrame as a new Excel file
    output_path = os.path.join(source_folder, output_filename)
    combined_df.to_excel(output_path, index=False, header=False)
    
    print(f"Combined data saved to: {output_path}")
    return combined_df

# Usage
if __name__ == "__main__":
    # Set the folder path where the aggregated Excel files are stored
    source_folder = r"E:\01-MFCC\aggregated_csvs"  # Replace with your folder path
    
    # Set the name of the output Excel file to be saved
    output_filename = "combined_aggregated_features.xlsx"
    
    # Load, combine, and save the data (include_artist_label=True to input artist name once)
    combined_data = load_and_save_aggregated_features(source_folder, output_filename, include_artist_label=True)
    
    # Display the shape of the combined DataFrame
    print("Shape of the combined dataset:", combined_data.shape)
    print(combined_data.head())  # Display the first few rows
