import mysql.connector
import pandas as pd
import plotly.graph_objects as go
from flask import Flask, render_template_string, request
from db_con import db_connect  
from formHandler import *


# Initialize Flask app
app = Flask(__name__)

# Define the route for the web app
@app.route('/map', methods=['GET', 'POST'])
def index():
    # Connect to the database
    db_config = db_connect()
    conn = mysql.connector.connect(**db_config)
    
    # Fetch latitude and longitude from the database using pandas
    tb = "lmia_tb"
    
    # Get filter values
    filterProvince = request.form.getlist('province')
    filterJob = request.form.getlist('jobCode')

    query = queryHandler(filterProvince,filterJob)

    
 # Execute the query and fetch data
    coordinates = pd.read_sql(query, conn) #To create map
    employers_list = coordinates[['employer', 'province', 'address', 'occ', 'requested_lmia']].values.tolist()
    coordinates['hover_info'] = (coordinates['employer'] + '<br>' +coordinates['address'] + '<br> code: ' +coordinates['occ']  )
    


    # Fech from database to create drop-down list for filter function
    checkBoxProvince = f""" SELECT DISTINCT province FROM {tb}"""
    province_list =  pd.read_sql(checkBoxProvince, conn) # to create dropdown list
    province_values = province_list[['province']].values.tolist()
    
    checkBoxJobCode = f""" SELECT DISTINCT occupation FROM {tb} ORDER BY LEFT(occupation, 4) """
    job_list =  pd.read_sql(checkBoxJobCode, conn) # to create dropdown list
    jobCode_values = job_list[['occupation']].values.tolist()
   
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
                <title>Employer Locations </title>
                <style>
                    .container {
                        display: flex;                 
                        margin: 20px;              
                    }
                    .box {
                        padding: 20px;                 
                        border: 1px solid #ccc;         
                        background-color: #f2f2f2;     
                        height: 150px;
                        overflow-y: auto;
                    }
            </style>
                                  
            </head>
            <body>
                <h1>Employer Locations </h1>
                <div style="border: 3px solid gray">{{ graph_html|safe }}</div>
                
                <h2>Filter</h2>
                <form method="post">
                                  
                    <div class="container" >
                        <div class = "box" >
                            {% for value in province_values %}
                            <input type="checkbox" name="province" value="{{ value[0] }}" />
                            <label for="province"> {{value[0]}}</label><br>
                            {% endfor %}
                        </div>
                        <div class="box" >
                            {% for value in jobCode_values %}
                            <input type="checkbox" name="jobCode" value="{{ value[0] }}" />
                            <label for="jobCode"> {{value[0]}}</label><br>
                            {% endfor %}
                        </div>
                    </div>
                    <input type="submit" value="Filter" name="filter" />
                    <input type="submit" name="reset" value="Reset" formaction="/map" />
                </form>

                <h2>List of Employers</h2>
                <div style="height: 500px;overflow-y: auto;" >
                    <table>
                        <tr>
                            <th>Company Name</th>
                            <th>Province / Territories</th>
                            <th>Address</th>
                            <th>NOC code</th>
                            <th>Total number of Requested LMIA from employer</th>
                        </tr>
                        {% for employer in employers_list %}
                            <tr><td>{{ employer[0] }}</td>
                                <td>{{ employer[1] }}</td>
                                <td>{{ employer[2] }}</td>
                                <td>{{ employer[3] }}</td>
                                <td>{{ employer[4] }}</td>
                            </tr>
                        {% endfor %}
                    </table>
                </div>
            </body>
        </html>
    ''', graph_html=graph_html, employers_list=employers_list, province_values=province_values, jobCode_values=jobCode_values)

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Expose on port 5000
