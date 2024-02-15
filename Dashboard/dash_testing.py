# Import required libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Dashboard with Expected Return Input"),
    dcc.Slider(
        id='expected-return-slider',
        min=0,
        max=20,
        step=0.5,
        value=10,
        marks={i: str(i) for i in range(0, 21, 2)},
    ),
    html.Div(id='slider-output-container'),
    dcc.Graph(id='line-chart'),
    dcc.Graph(id='bar-chart'),
    dcc.Graph(id='scatter-plot'),
    dcc.Graph(id='pie-chart'),
])

# Callback to update slider output
@app.callback(
    Output('slider-output-container', 'children'),
    [Input('expected-return-slider', 'value')])
def update_output(value):
    return f'Expected Return: {value}%'

# Callbacks to update charts based on the slider input
@app.callback(
    [Output('line-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('scatter-plot', 'figure'),
     Output('pie-chart', 'figure')],
    [Input('expected-return-slider', 'value')])
def update_charts(expected_return):
    # Generate sample data for charts
    x = np.arange(10)
    y = np.random.rand(10) * expected_return

    # Line Chart
    line_chart = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))

    # Bar Chart
    bar_chart = go.Figure(data=go.Bar(x=x, y=y))

    # Scatter Plot
    scatter_plot = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))

    # Pie Chart - Just a placeholder for demonstration
    pie_chart = go.Figure(data=go.Pie(labels=['A', 'B', 'C', 'D'], values=y[:4]))

    return line_chart, bar_chart, scatter_plot, pie_chart

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
