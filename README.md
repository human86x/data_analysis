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
## Acknowledgements

This dataset was sourced from the study by Zhang et al. (2019) on water quality monitoring using IoT networks. For further details on data collection and methodology, see the following publication:

- Zhang, Y. F., Thorburn, P. J., Xiang, W., & Fitch, P. (2019). SSIM—A deep learning approach for recovering missing time series sensor data. *IEEE Internet of Things Journal, 6*(4), 6618-6628.
