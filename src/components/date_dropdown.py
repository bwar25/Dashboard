from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd

from . import ids

csv_filepath = None
DATA = pd.read_csv(csv_filepath)
successful_charges_dates = DATA.Year.values.tolist()
successful_charges_dates = list(dict.fromkeys(successful_charges_dates))

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.SUCCESSFUL_CHARGES_DATES_DROPDOWN, "value"),
        Input(ids.SELECT_SUCCESSFUL_CHARGES_DATES_BUTTON, "n_clicks")
    )
    def select_successful_charges_dates(_: int) -> list[str]:
        return successful_charges_dates

    return html.Div(
        children=[
            html.H3("Years"),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_SUCCESSFUL_CHARGES_DATES_BUTTON
            ),
            dcc.Dropdown(
                id=ids.SUCCESSFUL_CHARGES_DATES_DROPDOWN,
                options=[{"label": date, "value": date} for date in successful_charges_dates],
                value=successful_charges_dates,
                multi=True,
            ),
        ]
    )
