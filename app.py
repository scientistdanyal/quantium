# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import os
from pathlib import Path


BASE_DIR = Path(__file__).parent

data = []


DATA_PATH = BASE_DIR/"ping_morsel_sales.csv"

df = pd.read_csv(DATA_PATH)

df["date"] = pd.to_datetime(df["date"])

daily_sales = (
    df.groupby("date", as_index=False)["sales"].sum().sort_values(by="date")
)




fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Daily Sales",
    labels={
        "date": "Date", 
        "sales": "Total Sales ($)",
        "region": "Region"
    },
)


fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red",
)

fig.add_annotation(
    x="2021-01-15",
    y=1,
    yref="paper",
    text="Sales increase",
    showarrow=False,
    xanchor="left",
)

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options



app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)