from dash import Dash, html
from dash.dependencies import Input, Output
import pandas as pd

from . import ids

csv_filepath = None
DATA = pd.read_csv(csv_filepath)

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.SUCCESSFUL_CHARGES_SUM_AMOUNT, 'children'),
        Input(ids.SUCCESSFUL_CHARGES_DATES_DROPDOWN, 'value')
    )
    def update_output_div(successful_charges_dates: list[str]) -> html.Div:
        filtered_data = DATA.query("Year in @successful_charges_dates")
        return f"Total: ${round(filtered_data['Amount'].sum(), 2)}"

    return html.Div(id=ids.SUCCESSFUL_CHARGES_SUM_AMOUNT)