import dash
from dash import html, dcc
import plotly.express as px

app = dash.Dash(__name__)

# Layout temporal
app.layout = html.Div([html.H1("Cargando...")])

def graphs(extractedData):
    if len(extractedData) < 6:
        print("extractedData no tiene suficientes datasets aún")
        return

    hiresByCountryYear = extractedData[0][0]    
    hiresByMonthYear = extractedData[1][0]      
    hiresBySeniority = extractedData[2][0]      
    hiresByTechnology = extractedData[3][0]     
    hiresByYear = extractedData[4][0]           
    applicationsVsHiresByYear = extractedData[5][0]
    hiresBYCountry = extractedData[6][0]

    fig_tech = px.pie(
        hiresByTechnology,
        names='Technology',
        values='Hires',
        title='Hires by Technology'
    )

    fig_year = px.bar(
        hiresByYear,
        x='Year',
        y='Hires',
        title='Hires by Year'
    )

    fig_seniority = px.line_polar(
        hiresBySeniority,
        theta='Seniority',
        r='Hires',
        line_close=True,
        title='Hires by Seniority'
    )

    fig_country_year = px.area(
        hiresByCountryYear,
        x='Year',
        y='Hires',
        color='Country',
        title='Hires by Country over Years'
    )

    fig_month_year = px.area(
        hiresByMonthYear,
        color='Month',
        y='Hires',
        x='Year',
        title='Hires by Month and Year'
    )

    fig_nothires_vs_hires = px.bar(
        applicationsVsHiresByYear,
        y=['TotalNotHires', 'TotalHires'],
        x='Technology',
        title='Not hires vs Hires'
    )
    fig_nothires_vs_hires.update_layout(barmode="stack")

    fig_hires_by_country = px.scatter_geo(
        hiresBYCountry,
        locations="Country", 
        locationmode="country names",
        size="Hires",       
        color="Hires",         
        projection="natural earth"
    )

    # Layout final
    app.layout = html.Div([
        html.H1('ETL Workshop - Data Engineer KPIs'),
        dcc.Graph(figure=fig_tech),
        dcc.Graph(figure=fig_year),
        dcc.Graph(figure=fig_seniority),
        dcc.Graph(figure=fig_country_year),
        dcc.Graph(figure=fig_month_year),
        dcc.Graph(figure=fig_nothires_vs_hires),
        dcc.Graph(figure=fig_hires_by_country)
    ])
