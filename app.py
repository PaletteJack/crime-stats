import dash
import dash_core_components as dcc
import dash_html_components as html
from charts import table_summary

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Chicago Crime Stats"),
    dcc.Graph(
        figure=table_summary()
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)