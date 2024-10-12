import mysql.connector
import pandas as pd
import plotly.graph_objects as go
from flask import Flask, render_template_string, request
from db_con import db_connect  # Ensure this module has your database connection logic

# Initialize Flask app
app = Flask(__name__)

# Define the route for the web app
@app.route('/', methods=['GET', 'POST'])
def index():
    # Connect to the database
    db_config = db_connect()
    conn = mysql.connector.connect(**db_config)
    
    # Fetch latitude and longitude from the database using pandas
    tb = "lmia_tb"
    
    # Get province input from the form
    province = request.form.get('province', '')  # Default to an empty string if not provided
    occupation = request.form.get('occupation', '')

    # Build SQL query based on occupation input
    if occupation:
        query = f"""
        SELECT latitude, longitude, employer, province, requested_lmia, address, LEFT(occupation, 4) AS occ FROM {tb} WHERE occupation LIKE '{occupation}%';
        """
    else:
        query = f"""
        SELECT latitude, longitude, province, employer, address, requested_lmia, LEFT(occupation, 4) AS occ FROM {tb};
        """
    
    # Execute the query and fetch data
    coordinates = pd.read_sql(query, conn) #To create map
    employers_list = coordinates[['employer', 'province', 'address', 'requested_lmia']].values.tolist()
    coordinates['hover_info'] = (coordinates['employer'] + '<br>' +coordinates['address'] + '<br> code: ' +coordinates['occ']  )
    
    # Create the Plotly figure
    fig = go.Figure(data=go.Scattergeo(
        lon=coordinates['longitude'],
        lat=coordinates['latitude'],
        text=coordinates['hover_info'],
        mode='markers',
        hoverinfo='text'
    ))

    fig.update_layout(
        title='Maps of LMIA Negative Employers',
        geo_scope='north america',
        height=500, margin={"r":0,"t":50,"l":0,"b":0}
    )
    fig.update_geos(
        visible=True,
        resolution=50,
        showcountries=True,
        countrycolor="Black",
        showsubunits=True,
        subunitcolor="Gray",
        center=dict(lat=55, lon=-97),  # Center the map on Canada
        projection_scale=2,  # Zoom 
    )

    # Convert the Plotly figure to HTML
    graph_html = fig.to_html(full_html=False)

    # Close the database connection
    conn.close()

    # Render the HTML page with both the map and the list of employers
    return render_template_string('''
        <html>
            <head>
                <title>Employer Locations</title>
            </head>
            <body>
                <h1>Employer Locations</h1>
                <div style="border: 3px solid gray">{{ graph_html|safe }}</div>
                
                <h2>Filters by Occupation</h2>
                <form method="post">
                    <input type="text" name="occupation" placeholder="4 digit occupation code" />
                    <input type="submit" value="Search" />
                    <input type="submit" name="reset" value="Reset" formaction="/" />
                </form>

                <h2>List of Employers</h2>
                <div>
                    <table>
                        <tr>
                            <th>Company Name</th>
                            <th>Province / Territories</th>
                            <th>Address</th>
                            <th>Requested LMIA</th>
                        </tr>
                        {% for employer in employers_list %}
                            <tr><td>{{ employer[0] }}</td>
                                <td>{{ employer[1] }}</td>
                                <td>{{ employer[2] }}</td>
                                <td>{{ employer[3] }}</td>
                            </tr>
                        {% endfor %}
                    </table>
                </div>
            </body>
        </html>
    ''', graph_html=graph_html, employers_list=employers_list)

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Expose on port 5000
