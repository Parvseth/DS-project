import os
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

def aggregate_mfcc(mfcc):
    """
    Aggregate MFCC matrix to extract multiple statistical features.
    Features include:
    - Mean, Standard Deviation, Minimum, Maximum
    - Median, Range, Interquartile Range (IQR)
    - Skewness, Kurtosis, Energy, Root Mean Square (RMS)
    """
    features = []
    
    # Mean, Standard Deviation, Min, Max for each row (MFCC coefficient)
    features.append(np.mean(mfcc, axis=1))          # Mean
    features.append(np.std(mfcc, axis=1))           # Standard Deviation
    features.append(np.min(mfcc, axis=1))           # Minimum
    features.append(np.max(mfcc, axis=1))           # Maximum
    
    # Additional features
    features.append(np.median(mfcc, axis=1))        # Median
    features.append(np.ptp(mfcc, axis=1))           # Range (Max - Min)
    features.append(np.percentile(mfcc, 75, axis=1) - np.percentile(mfcc, 25, axis=1))  # IQR (Interquartile Range)
    features.append(np.sum(mfcc**2, axis=1))        # Energy
    features.append(np.sqrt(np.mean(mfcc**2, axis=1)))  # Root Mean Square (RMS)
    
    # Skewness and Kurtosis (Using scipy.stats)
    features.append(skew(mfcc, axis=1, nan_policy='omit'))    # Skewness
    features.append(kurtosis(mfcc, axis=1, nan_policy='omit')) # Kurtosis
    
    # Concatenate all features into a single array
    return np.concatenate(features)

def process_and_save_aggregated_features(source_folder, destination_folder):
    """
    Process each CSV file to extract aggregated MFCC features and save them to new Excel files.
    """
    os.makedirs(destination_folder, exist_ok=True)
    
    # Get all CSV files in the source folder
    csv_files = [f for f in os.listdir(source_folder) if f.endswith('.csv')]
    
    for file_name in csv_files:
        # Load the padded MFCC matrix from CSV
        file_path = os.path.join(source_folder, file_name)
        df = pd.read_csv(file_path, header=None)
        mfcc = df.values
        
        # Aggregate the MFCC features
        aggregated_features = aggregate_mfcc(mfcc)
        
        # Convert the aggregated features to a DataFrame (each feature in a single row)
        aggregated_df = pd.DataFrame(aggregated_features).transpose()
        
        # Save the aggregated features to a new Excel file
        output_filename = f"aggregated_{os.path.splitext(file_name)[0]}.xlsx"
        output_path = os.path.join(destination_folder, output_filename)
        aggregated_df.to_excel(output_path, index=False, header=False)
        
        print(f"Processed and saved aggregated features: {output_filename}")

# Usage
if __name__ == "__main__":
    # Set the folder paths
    source_folder = r"E:\01-MFCC\padded_csvs"  # Folder containing your padded CSV files
    destination_folder = r"E:\01-MFCC\aggregated_csvs"  # Folder to save the Excel files

    # Process and save aggregated features
    process_and_save_aggregated_features(source_folder, destination_folder)
