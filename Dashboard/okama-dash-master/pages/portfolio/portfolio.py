from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from app_instance import app  

# Sample data: stocks and their weightings
stocks_data = {
    'Stock': ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB'],
    'Weighting': [20, 30, 25, 15, 10]
}
df = pd.DataFrame(stocks_data)

# Calculate summary statistics
mean_weighting = df['Weighting'].mean()
median_weighting = df['Weighting'].median()
std_dev_weighting = df['Weighting'].std()

# Define the layout for this page
layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            html.H1("Stock Portfolio Weightings", className="text-center"),
            width=12
        )
    ),
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id='stock-dropdown',
                options=[{'label': stock, 'value': stock} for stock in df['Stock']],
                value=['AAPL'],  # Default value
                multi=True,  # Allow multiple selections
                className="mb-3",  # Margin bottom
            ),
            md=6,  # Use 6 columns width on medium or larger devices
        )
    ]),
    dbc.Row(
        dbc.Col(
            dcc.Graph(id='pie-chart'),
            width=12
        )
    ),
    # New Row for Summary Statistics
    dbc.Row([
        dbc.Col(html.Div(f"Mean Weighting: {mean_weighting:.2f}"), md=4),
        dbc.Col(html.Div(f"Median Weighting: {median_weighting:.2f}"), md=4),
        dbc.Col(html.Div(f"Standard Deviation: {std_dev_weighting:.2f}"), md=4),
    ], className="mb-4"),  # Add some bottom margin
], fluid=True)

# Callback to update pie chart based on selected stocks
@app.callback(
    Output('pie-chart', 'figure'),
    [Input('stock-dropdown', 'value')]
)
def update_pie_chart(selected_stocks):
    filtered_df = df[df['Stock'].isin(selected_stocks)]
    fig = px.pie(filtered_df, values='Weighting', names='Stock', title='Stock Weightings')
    return fig