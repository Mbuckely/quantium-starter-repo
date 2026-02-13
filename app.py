from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Load and prepare data
df = pd.read_csv("formatted_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

regional_sales = (
    df.groupby(["Date", "Region"], as_index=False)["Sales"]
    .sum()
    .sort_values("Date")
)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Before and After Price Increase"),

    dcc.Dropdown(
        id="region-dropdown",
        options=[
            {"label": "All Regions", "value": "ALL"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="ALL"
    ),

    dcc.Graph(id="sales-graph")
])

# Callback
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-dropdown", "value")
)
def update_graph(selected_region):

    if selected_region == "ALL":
        filtered_df = regional_sales
    else:
        filtered_df = regional_sales[
            regional_sales["Region"] == selected_region
        ]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region" if selected_region == "ALL" else None,
        title="Pink Morsel Sales Over Time",
        labels={
            "Date": "Date",
            "Sales": "Total Sales"
        }
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)



#run this in terminal to see dash -> pip install dash then -> python app.py


