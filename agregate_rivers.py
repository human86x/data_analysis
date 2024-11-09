import pandas as pd
import os

# Directory containing river data files
data_dir = "/home/human/git_data/data/rivers"

# Output file
output_file = "/home/human/git_data/data/processed/aggregated_river_data.csv"

# Mapping of file names to river name and location
river_info = {
    "Johnstone_river_coquette_point_joined.csv": ("Johnstone River", "Coquette Point"),
    "Johnstone_river_innisfail_joined.csv": ("Johnstone River", "Innisfail"),
    "Mulgrave_river_deeral_joined.csv": ("Mulgrave River", "Deeral"),
    "Pioneer_Dumbleton_joined.csv": ("Pioneer River", "Dumbleton"),
    "Plane_ck_sucrogen_joined.csv": ("Plane Creek", "Sucrogen"),
    "Proserpine_river_glen_isla_joined.csv": ("Proserpine River", "Glen Isla"),
    "russell_river_east_russell_joined.csv": ("Russell River", "East Russell"),
    "sandy_ck_homebush_joined.csv": ("Sandy Creek", "Homebush"),
    "sandy_ck_sorbellos_road_joined.csv": ("Sandy Creek", "Sorbellos Road"),
    "Tully_river_euramo_joined.csv": ("Tully River", "Euramo"),
    "Tully_River_Tully_Gorge_National_Park_joined.csv": ("Tully River", "Tully Gorge National Park")
}

# List to store dataframes
dataframes = []

# Define the final target column order
target_columns = ['Timestamp', 'Conductivity', 'NO3', 'Temp', 'Turbidity', 'Dayofweek', 'Month', 'Q', 'Level', 'River Name', 'Location']

# Process each file
for file_name, (river_name, location) in river_info.items():
    file_path = os.path.join(data_dir, file_name)
    df = pd.read_csv(file_path)
    
    # Add river-specific information
    df["River Name"] = river_name
    df["Location"] = location
    
    # Initialize an empty DataFrame with the target columns
    aligned_df = pd.DataFrame(columns=target_columns)
    
    # Copy data from the current file's DataFrame to the aligned DataFrame
    for column in df.columns:
        if column in target_columns:
            aligned_df[column] = df[column]
    
    # Fill missing columns with NaN (for columns not present in the file)
    aligned_df["River Name"] = river_name
    aligned_df["Location"] = location
    
    # Append to the list of dataframes
    dataframes.append(aligned_df)

# Concatenate all dataframes
aggregated_df = pd.concat(dataframes, ignore_index=True)

# Save to CSV
aggregated_df.to_csv(output_file, index=False)

print(f"Aggregated data saved to {output_file}")
