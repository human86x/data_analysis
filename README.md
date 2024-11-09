# Water Quality Data Analysis Project

This project uses real-time data collected from various in-situ water quality monitoring stations in North Queensland, Australia, to gain insights into water quality indicators over time. The dataset supports tasks such as water quality forecasting, missing data imputation, and outlier detection, making it a valuable tool for environmental, agricultural, and industrial monitoring.

## Dataset Overview

The dataset includes data from 11 monitoring stations across rivers in North Queensland, Australia. Each station measures key water quality parameters such as:
- Water level
- Water temperature
- Electrical conductivity
- Turbidity
- Nitrate concentration
- Water discharge

The dataset is pre-processed to remove outliers and is resampled for consistency. Data collection periods may vary between stations due to different sensor deployment and replacement times.

Data files included:
- `Johnstone_river_coquette_point_joined.csv`
- `Johnstone_river_innisfail_joined.csv`
- `Mulgrave_river_deeral_joined.csv`
- `Pioneer_Dumbleton_joined.csv`
- `Plane_ck_sucrogen_joined.csv`
- `Proserpine_river_glen_isla_joined.csv`
- `Tully_River_Tully_Gorge_National_Park_joined.csv`
- `Tully_river_euramo_joined.csv`
- `russell_river_east_russell_joined.csv`
- `sandy_ck_homebush_joined.csv`
- `sandy_ck_sorbellos_road_joined.csv`

## Project Structure

- **initial.py**: A script to initially load and visualize each dataset, providing summaries on column types, missing data, and statistical information for numeric columns.
- **agregate_rivers.py**: Aggregates data from individual rivers into a single `aggregated_river_data.csv` file, preserving information on river names and locations.
- **app.py**: Implements a data visualization dashboard using Dash and Dash Leaflet, allowing users to interactively explore water quality data. Key features include:
  - A dropdown menu to select specific metrics for time-series visualization.
  - Interactive maps with markers for each river station.
  - Individual bar charts showing average water quality metrics by river station.

## Data Processing Workflow

1. **Initial Data Exploration** (`initial.py`):
   - Loads and provides a summary for each dataset file.
   - Displays key statistics and identifies any missing values or outliers.

2. **Data Aggregation** (`agregate_rivers.py`):
   - Aggregates data across river stations into a unified format.
   - Aligns columns across files and adds metadata columns for each river’s name and location.

3. **Data Visualization** (`app.py`):
   - Displays time-series plots for selected water quality metrics.
   - Provides a map view with each river station’s geographical location.
   - Offers bar charts summarizing average metrics (Conductivity, Temperature, Nitrate, Turbidity, Discharge, Water Level) for each station.

## Running the Application

To start the data visualization app, run the following command in the terminal:

```bash
python app.py
```
## Dependencies

Make sure to have all dependencies installed, such as:

- `pandas`
- `dash`
- `dash_leaflet`
- `plotly`

You can install them using pip:

```bash
pip install pandas dash dash-leaflet plotly
```


##Step 1: Understanding the Files
In the first step, we need to analyze the dataset files to check their consistency, column structure, and how well the data fits together. The goal here is to identify how many rows are in each file, check if there are any missing values, and verify the columns that exist in each file.
###Loading the Files:
```bash
import pandas as pd
import os

# Directory containing river data files
data_dir = "/home/human/git_data/data/rivers"
```
In this part of the script, we import the necessary pandas library, which will be used for data manipulation, and the os library to handle file paths.
We define the directory (data_dir) where all the river data files are stored. This allows us to point the script to the correct location where our data files are stored.
Listing the Files:
```bash
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
```
Here, we define the river_files list, which contains the names of all the CSV files to be processed. Each file corresponds to a river monitoring station, with the data for various water quality parameters.
Step 2: Reading Each File and Inspecting Data
For each file, we will read the contents into a pandas DataFrame and examine the basic structure of the data.
Code for Looping through Files and Reading Data:
```bash
# Process each file
for file_name in river_files:
    file_path = os.path.join(data_dir, file_name)
    print(f"Processing {file_name}...")
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
```
Here, we loop through the river_files list. For each file, we construct the full file path using os.path.join() to ensure compatibility across different operating systems.
Next, the pd.read_csv() function is used to load each CSV file into a pandas DataFrame, which allows us to interact with the data more easily.
Basic Summary and Initial Checks:
```bash
    # Print basic information
    print(f"--- Summary for {file_name} ---")
    print("Basic Information:")
    print(f"Columns: {df.columns}")
    print(f"Data Types:\n{df.dtypes}")
```
Here, we print basic information about the dataset:
    • Columns: The names of the columns in the dataset.
    • Data Types: The data types of each column (e.g., integer, float, datetime, etc.).
Displaying the First Few Rows:
```bash
    # Display the first few rows of the dataset
    print("\nFirst few rows:")
    print(df.head())
```
Using df.head(), we display the first few rows of the dataset to get an idea of the structure and the values contained within each column. This helps us verify if the data looks as expected, especially for the first few entries.
Checking Missing Data:
```bash
    # Print missing data summary
    print("\nMissing Data:")
    print(df.isnull().sum())
```
Here, we use df.isnull().sum() to check for missing data in the dataset. This method will give us a summary of the number of missing values in each column. If any columns have a significant amount of missing data, it might indicate data quality issues.
Statistical Summary:
```bash
    # Print statistical summary for numeric columns
    print("\nStatistical Summary (for numeric columns):")
    print(df.describe())
    
    print("\n" + "="*50 + "\n")
```
The df.describe() function is used to generate a statistical summary of the numeric columns, which includes metrics like the mean, standard deviation, minimum, and maximum values. This helps identify outliers or unusual data points.

Step 3: Output
Each file is processed in turn, and a summary of its basic structure, missing values, and statistical overview is printed. This initial inspection helps determine:
    • The quality of the data (e.g., missing or incomplete records).
    • The presence of any unexpected columns or data types.
    • A sense of the distribution of values (e.g., extremely high or low values, which might indicate outliers).

Summary
The initial.py script serves as the first step in exploring and preparing the data. By loading the dataset files, inspecting the structure, checking for missing data, and calculating basic statistics, it gives you a clear picture of the dataset's state. Based on this output, you can make informed decisions about how to proceed with data cleaning and aggregation.






## Acknowledgements

This dataset was sourced from the study by Zhang et al. (2019) on water quality monitoring using IoT networks. For further details on data collection and methodology, see the following publication:

- Zhang, Y. F., Thorburn, P. J., Xiang, W., & Fitch, P. (2019). SSIM—A deep learning approach for recovering missing time series sensor data. *IEEE Internet of Things Journal, 6*(4), 6618-6628.
