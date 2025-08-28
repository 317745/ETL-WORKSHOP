import dash
from dash import dcc, html
import plotly.express as px

app = dash.Dash(__name__)

extractedData = []

def serve_layout():
    graphs = []
    for name, df in extractedData:
        if not df.empty:
            cols = df.columns.tolist()
            if len(cols) >= 2:
                fig = px.bar(df, x=cols[0], y=cols[1])
                graphs.append(html.Div([
                    html.H3(name),
                    dcc.Graph(figure=fig)
                ]))
    return html.Div(children=graphs)

app.layout = serve_layout
