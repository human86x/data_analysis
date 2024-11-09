import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_leaflet as dl
import plotly.express as px

# Load your river data
rivers_data = pd.read_csv('/home/human/git_data/data/processed/aggregated_river_data.csv')

# Sample data for rivers and their coordinates
river_coordinates = {
    "Johnstone River Coquette Point": (-17.6342, 146.0341),
    "Johnstone River Innisfail": (-17.5371, 146.0310),
    "Mulgrave River Deeral": (-17.1935, 145.7225),
    "Pioneer River Dumbleton": (-21.1343, 149.1767),
    "Plane Creek Sucrogen": (-21.4747, 149.2940),
    "Proserpine River Glen Isla": (-20.4265, 148.5848),
    "Russell River East Russell": (-17.1850, 145.8327),
    "Sandy Creek Homebush": (-20.2470, 148.8824),
    "Sandy Creek Sorbellos Road": (-20.3538, 148.9022),
    "Tully River Euramo": (-17.6432, 145.9498),
    "Tully River Tully Gorge National Park": (-17.5980, 145.6773)
}

# Create a Dash app
app = Dash(__name__)

# Define available metrics, excluding unwanted options
excluded_metrics = ['River Name', 'Location', 'Dayofweek', 'Month', 'Timestamp']  # Added 'Timestamp' to the excluded list
metrics = [col for col in rivers_data.columns if col not in excluded_metrics]

# Define unique rivers
rivers = rivers_data['River Name'].unique()

# Calculate average values for each metric
average_metrics = {
    'Conductivity': rivers_data.groupby('River Name')['Conductivity'].mean().reset_index(),
    'Temp': rivers_data.groupby('River Name')['Temp'].mean().reset_index(),
    'NO3': rivers_data.groupby('River Name')['NO3'].mean().reset_index(),
    'Turbidity': rivers_data.groupby('River Name')['Turbidity'].mean().reset_index(),
    'Q': rivers_data.groupby('River Name')['Q'].mean().reset_index(),
    'Level': rivers_data.groupby('River Name')['Level'].mean().reset_index()
}

# Define a color mapping for each metric
color_mapping = {
    'Conductivity': 'blue',      # Blue for conductivity (water quality)
    'Temp': 'orange',            # Orange for temperature (warmth)
    'NO3': 'green',              # Green for nitrate (nature)
    'Turbidity': 'brown',        # Brown for turbidity (sediment)
    'Q': 'purple',               # Purple for discharge (flow)
    'Level': 'cyan'              # Cyan for water level (depth)
}

app.layout = html.Div([
    dcc.Dropdown(
        id='metric-dropdown',
        options=[{'label': metric, 'value': metric} for metric in metrics],
        value=metrics[0]  # Default value
    ),
    dcc.Graph(id='metric-graph'),
    
    # Map below the running chart with smaller size
    dl.Map(center=(-20, 146), zoom=6, style={'width': '100%', 'height': '400px'}, children=[
        dl.TileLayer(),
        *[dl.Marker(
            position=(lat, lon),
            id=river_name,
            children=[
                dl.Tooltip(river_name),  # Tooltip showing river name
                dl.Popup(river_name)      # Popup showing river name
            ]
        ) for river_name, (lat, lon) in river_coordinates.items()]
    ]),
    
    # Group the bar charts into rows of two
    html.Div(style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'space-around'}, children=[
        html.Div(
            style={'width': '48%', 'margin': '1%'},
            children=[
                dcc.Graph(
                    id='conductivity-bar-chart',
                    figure=px.bar(
                        average_metrics['Conductivity'],
                        x='River Name',
                        y='Conductivity',
                        title='Average Conductivity by River',
                        color_discrete_sequence=[color_mapping['Conductivity']]  # Use specific color
                    )
                )
            ]
        ),
        html.Div(
            style={'width': '48%', 'margin': '1%'},
            children=[
                dcc.Graph(
                    id='temperature-bar-chart',
                    figure=px.bar(
                        average_metrics['Temp'],
                        x='River Name',
                        y='Temp',
                        title='Average Temperature by River',
                        color_discrete_sequence=[color_mapping['Temp']]  # Use specific color
                    )
                )
            ]
        ),
        html.Div(
            style={'width': '48%', 'margin': '1%'},
            children=[
                dcc.Graph(
                    id='no3-bar-chart',
                    figure=px.bar(
                        average_metrics['NO3'],
                        x='River Name',
                        y='NO3',
                        title='Average NO3 by River',
                        color_discrete_sequence=[color_mapping['NO3']]  # Use specific color
                    )
                )
            ]
        ),
        html.Div(
            style={'width': '48%', 'margin': '1%'},
            children=[
                dcc.Graph(
                    id='turbidity-bar-chart',
                    figure=px.bar(
                        average_metrics['Turbidity'],
                        x='River Name',
                        y='Turbidity',
                        title='Average Turbidity by River',
                        color_discrete_sequence=[color_mapping['Turbidity']]  # Use specific color
                    )
                )
            ]
        ),
        html.Div(
            style={'width': '48%', 'margin': '1%'},
            children=[
                dcc.Graph(
                    id='q-bar-chart',
                    figure=px.bar(
                        average_metrics['Q'],
                        x='River Name',
                        y='Q',
                        title='Average Q by River',
                        color_discrete_sequence=[color_mapping['Q']]  # Use specific color
                    )
                )
            ]
        ),
        html.Div(
            style={'width': '48%', 'margin': '1%'},
            children=[
                dcc.Graph(
                    id='level-bar-chart',
                    figure=px.bar(
                        average_metrics['Level'],
                        x='River Name',
                        y='Level',
                        title='Average Level by River',
                        color_discrete_sequence=[color_mapping['Level']]  # Use specific color
                    )
                )
            ]
        )
    ])
])

@app.callback(
    Output('metric-graph', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_graph(selected_metric):
    # Create a figure for the selected metric
    fig = px.line(rivers_data, x='Timestamp', y=selected_metric, color='River Name')
    return fig

@app.callback(
    Output('conductivity-bar-chart', 'figure'),
    Output('temperature-bar-chart', 'figure'),
    Output('no3-bar-chart', 'figure'),
    Output('turbidity-bar-chart', 'figure'),
    Output('q-bar-chart', 'figure'),
    Output('level-bar-chart', 'figure'),
    [Input('metric-graph', 'clickData')]
)
def highlight_bars(clickData):
    highlighted_river = clickData['points'][0]['customdata'] if clickData else None
    
    # Create figures with highlighted bars if a river is selected
    figures = []
    for metric in average_metrics.keys():
        bar_fig = px.bar(
            average_metrics[metric],
            x='River Name',
            y=metric,
            title=f'Average {metric} by River',
            color_discrete_sequence=[color_mapping[metric]],
            opacity=0.5  # Make bars semi-transparent
        )
        if highlighted_river:
            bar_fig.for_each_trace(lambda t: t.update(marker=dict(opacity=1) if t.name == highlighted_river else dict(opacity=0.5)))
        figures.append(bar_fig)

    return figures

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
