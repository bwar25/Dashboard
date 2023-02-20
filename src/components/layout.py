from dash import Dash, html

from . import bar_chart
from . import date_dropdown
from . import sum_amount

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    date_dropdown.render(app)
                ]
            ),
            bar_chart.render(app),
            sum_amount.render(app),
        ]
    )