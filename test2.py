import plotly.graph_objects as go
import pandas as pd

# Sample data
data = {
    'lat': [45.4215, 49.2827, 43.6532, 52.9399],
    'lon': [-75.6972, -123.1207, -79.3832, -73.7004],
    'intensity': [10, 15, 20, 5],  # This could represent the intensity or count
    'city': ['Ottawa', 'Vancouver', 'Toronto', 'Quebec City']
}

df = pd.DataFrame(data)

# Create the Plotly figure
fig = go.Figure(data=go.Scattergeo(
    lon=df['lon'],
    lat=df['lat'],
    text=df['city'],
    marker=dict(
        size=df['intensity'] * 2,  # Scale the marker size based on intensity
        color=df['intensity'],
        colorscale='Viridis',  # You can choose a different colorscale
        showscale=True,  # Show the color scale bar
        colorbar=dict(title='Intensity'),
    ),
))

fig.update_layout(
    title='Geographical Heatmap',
    geo=dict(
        scope='north america',  # Set the region
        projection_type='natural earth',
        showland=True,
    )
)

fig.show()
