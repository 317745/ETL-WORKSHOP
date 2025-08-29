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

    # ✅ Los DataFrames ya vienen listos
    hiresByCountryYear = extractedData[0][0]    
    hiresByMonthYear = extractedData[1][0]      
    hiresBySeniority = extractedData[2][0]      
    hiresByTechnology = extractedData[3][0]     
    hiresByYear = extractedData[4][0]           
    applicationsVsHiresByYear = extractedData[5][0]

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

    fig_seniority = px.bar(
        hiresBySeniority,
        x='Seniority',
        y='Hires',
        title='Hires by Seniority'
    )

    fig_country_year = px.bar(
        hiresByCountryYear,
        x='Year',
        y='Hires',
        color='Country',
        barmode='group',
        title='Hires by Country over Years'
    )

    fig_month_year = px.bar(
        hiresByMonthYear,
        x='Month',
        y='Hires',
        title='Hires by Month in 2020'
    )

    # Pie especial para aplicaciones vs hires
    fig_apps_vs_hires = px.pie(
        names=['Total Applications', 'Total Hires'],
        values=[applicationsVsHiresByYear.TotalApplications, applicationsVsHiresByYear.TotalHires],
        title='Applications vs Hires'
    )

    # Layout final
    app.layout = html.Div([
        html.H1('ETL Workshop - Data Engineer KPIs'),
        dcc.Graph(figure=fig_tech),
        dcc.Graph(figure=fig_year),
        dcc.Graph(figure=fig_seniority),
        dcc.Graph(figure=fig_country_year),
        dcc.Graph(figure=fig_month_year),
        dcc.Graph(figure=fig_apps_vs_hires)
    ])
