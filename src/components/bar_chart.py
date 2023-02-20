from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

from . import ids

DATA = pd.read_csv('.\data\successful_charges.csv')

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.SUCCESSFUL_CHARGES_BAR_CHART, "children"),
        Input(ids.SUCCESSFUL_CHARGES_DATES_DROPDOWN, "value")
    )
    def update_bar_chart(successful_charges_dates: list[str]) -> html.Div:
        filtered_data = DATA.query("Year in @successful_charges_dates")

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected") 

        fig = px.bar(filtered_data, x="Date", y="Amount", color="Amount", text="Amount", title = 'Individual Sales (Stripe)')

        return html.Div(dcc.Graph(figure=fig), id=ids.SUCCESSFUL_CHARGES_BAR_CHART)

    return html.Div(id=ids.SUCCESSFUL_CHARGES_BAR_CHART)