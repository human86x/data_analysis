import pandas as pd
import os

# Directory containing river data files
data_dir = "/home/human/git_data/data/rivers"

# List of river data files
river_files = [
    "Johnstone_river_coquette_point_joined.csv",
    "Johnstone_river_innisfail_joined.csv",
    "Mulgrave_river_deeral_joined.csv",
    "Pioneer_Dumbleton_joined.csv",
    "Plane_ck_sucrogen_joined.csv",
    "Proserpine_river_glen_isla_joined.csv",
    "russell_river_east_russell_joined.csv",
    "sandy_ck_homebush_joined.csv",
    "sandy_ck_sorbellos_road_joined.csv",
    "Tully_river_euramo_joined.csv",
    "Tully_River_Tully_Gorge_National_Park_joined.csv"
]

# Process each file
for file_name in river_files:
    file_path = os.path.join(data_dir, file_name)
    print(f"Processing {file_name}...")
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Print basic information
    print(f"--- Summary for {file_name} ---")
    print("Basic Information:")
    print(f"Columns: {df.columns}")
    print(f"Data Types:\n{df.dtypes}")
    
    # Display the first few rows of the dataset
    print("\nFirst few rows:")
    print(df.head())
    
    # Print missing data summary
    print("\nMissing Data:")
    print(df.isnull().sum())
    
    # Print statistical summary for numeric columns
    print("\nStatistical Summary (for numeric columns):")
    print(df.describe())
    
    print("\n" + "="*50 + "\n")
