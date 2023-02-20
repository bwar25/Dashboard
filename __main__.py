from dash import Dash, html

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

from src.components.layout import create_layout

load_figure_template('SUPERHERO')

def main() -> None:
    app = Dash(external_stylesheets=[dbc.themes.SUPERHERO])
    app.title = "Dashboard"
    app.layout = create_layout(app)
    app.run_server(debug=True)

if __name__ == "__main__":
    main()