import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

from ..app import config_plots

def charts(clean_data):
    """
    Build the charts.

    This function uses the ``clean_data`` parameter
    and uses the data to build charts.

    Parameters
    ----------
    clean_data : dict of {str : int or pd.DataFrame}
        Dictionary that contains integers and pd.DataFrames to use as
        data in the charts.

    Returns
    -------
    dict
        Dictionary of Plotly charts.
    """
    chart_knob_1 = daq.Gauge(
                        id='my-gauge',
                        label="Default",
                        value=6,
                        style={'display': 'block' }
                        )

    return {"chart-knob-1": chart_knob_1,
            }


def app_content(charts, clean_data):
    """
    Build the html components.

    Use html components with ``charts`` parameters
    to build the layout of the dashboard.

    Parameters
    ----------
    charts : dict of {str : plotly.graph_objects or plotly.express}
        Dictionary that contains the charts.
    clean_data : dict of {str : int or pd.DataFrame}
        Dictionary that contains integers and pd.DataFrames, but the 
        integer values are used to build summary cards.

    Returns
    -------
    html.Div
        Div component of the dash_html_components.html.Div.
    """    
    df = px.data.stocks()
    fig_line_1 = px.line(df, x='date', y="GOOG")
    fig_line_1.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig_line_1.update_layout(
        paper_bgcolor='#303140',
        plot_bgcolor='#303140',
        font={'color':'white', "family":"Montserrat"},
        height=180,
        width=465,
        margin=dict(l=0, r=0, t=0, b=0),
    )

    chart_line_1 = [        
                dcc.Graph(figure=fig_line_1,
                animate=True, config=config_plots),
    ]



    fig_bar_1 = go.Figure()
    fig_bar_1.add_trace(go.Bar(
        name='Control',
        x=['Trial 1', 'Trial 2', 'Trial 3'], y=[3, 6, 4],
        error_y=dict(type='data', array=[1, 0.5, 1.5])
    ))
    fig_bar_1.add_trace(go.Bar(
        name='Experimental',
        x=['Trial 1', 'Trial 2', 'Trial 3'], y=[4, 7, 3],
        error_y=dict(type='data', array=[0.5, 1, 2])
    ))
    fig_bar_1.update_layout(
        barmode='group',
        paper_bgcolor='#303140',
        plot_bgcolor='#303140',
        font={'color':'white', "family":"Montserrat"},
        height=180,
        width=430,
        margin=dict(l=0, r=0, t=5, b=0),)

    chart_bar_1 = [        
                dcc.Graph(figure=fig_bar_1,
                animate=True, config=config_plots),
    ]



    df = px.data.tips()
    fig_sunburst_1 = px.sunburst(df, path=['day', 'time', 'sex'], values='total_bill')
    fig_sunburst_1.update_layout(margin = dict(t=0, l=0, r=0, b=0),
        paper_bgcolor='#303140',
        plot_bgcolor='#303140',
        font={'color':'white', "family":"Montserrat"},
        height=180,
        width=350,)

    chart_sunburst_1 = [        
                dcc.Graph(figure=fig_sunburst_1,
                animate=True, config=config_plots),
    ]



    size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]
    fig_bubble_1 = go.Figure(data=[go.Scatter(
        x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        y=[11, 12, 10, 11, 12, 11, 12, 13, 12, 11],
        mode='markers',
        marker=dict(
            size=size,
            sizemode='area',
            sizeref=2.*max(size)/(40.**2),
            sizemin=4
        )
    )])

    fig_bubble_1.update_layout(
        paper_bgcolor='#303140',
        plot_bgcolor='#303140',
        font={'color':'white', "family":"Montserrat"},
        height=180,
        width=465,
        margin=dict(l=0, r=0, t=0, b=0),
    )

    chart_bubble_1 = [        
                dcc.Graph(figure=fig_bubble_1,
                animate=True, config=config_plots),
    ]




    np.random.seed(1)

    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5

    # Create traces
    fig_lines_2 = go.Figure()
    fig_lines_2.add_trace(go.Scatter(x=random_x, y=random_y0,
                        mode='lines',
                        name='lines'))
    fig_lines_2.add_trace(go.Scatter(x=random_x, y=random_y1,
                        mode='lines+markers',
                        name='lines+markers'))
    fig_lines_2.add_trace(go.Scatter(x=random_x, y=random_y2,
                        mode='markers', name='markers'))

    fig_lines_2.update_layout(
        paper_bgcolor='#303140',
        plot_bgcolor='#303140',
        font={'color':'white', "family":"Montserrat"},
        height=180,
        width=465,
        margin=dict(l=0, r=0, t=0, b=0),
    )


    chart_lines_2 = [        
            dcc.Graph(figure=fig_lines_2,
            animate=True, config=config_plots),
    ]




    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December']
    high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
    low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
    high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
    low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
    high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
    low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

    fig_lines_3 = go.Figure()
    # Create and style traces
    fig_lines_3.add_trace(go.Scatter(x=month, y=high_2014, name='High 2014',
                            line=dict(color='firebrick', width=4)))
    fig_lines_3.add_trace(go.Scatter(x=month, y=low_2014, name = 'Low 2014',
                            line=dict(color='royalblue', width=4)))
    fig_lines_3.add_trace(go.Scatter(x=month, y=high_2007, name='High 2007',
                            line=dict(color='firebrick', width=4,
                                dash='dash') # dash options include 'dash', 'dot', and 'dashdot'
    ))
    fig_lines_3.add_trace(go.Scatter(x=month, y=low_2007, name='Low 2007',
                            line = dict(color='royalblue', width=4, dash='dash')))
    fig_lines_3.add_trace(go.Scatter(x=month, y=high_2000, name='High 2000',
                            line = dict(color='firebrick', width=4, dash='dot')))
    fig_lines_3.add_trace(go.Scatter(x=month, y=low_2000, name='Low 2000',
                            line=dict(color='royalblue', width=4, dash='dot')))

    fig_lines_3.update_layout(
        paper_bgcolor='#303140',
        plot_bgcolor='#303140',
        font={'color':'white', "family":"Montserrat"},
        height=180,
        width=545,
        margin=dict(l=0, r=0, t=0, b=0),
    )


    chart_lines_3 = [        
            dcc.Graph(figure=fig_lines_3,
            animate=True, config=config_plots),
    ]




    d = {'Predio':['Reitoria','STD','CEGEN','DELOGS'], 'Chamados': [3000, 4000, 5000, 6000], 'lat':['-8.014212','-8.018282','-8.017475','-8.015940'], 'lon':['-34.950411','-34.949333','-34.950096','-34.946378']}
    df = pd.DataFrame(data=d)
    df["lat"] = pd.to_numeric(df["lat"], downcast="float")
    df["lon"] = pd.to_numeric(df["lon"], downcast="float")

    df_diffq = (df["Chamados"].max() - df["Chamados"].min()) / 49
    df["scale"] = (df["Chamados"] - df["Chamados"].min()) / df_diffq + 30



    fig_map_1 = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="Predio", hover_data=["Chamados"],
                            color="Chamados", color_continuous_scale=px.colors.sequential.Oranges,
                            size=df["scale"], size_max=50, zoom=15, height=500)
    fig_map_1.update_layout(mapbox_style="open-street-map")
    fig_map_1.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor='#303140',
        plot_bgcolor='#303140',
        font={'color':'white', "family":"Montserrat"},
        width=935,
        height=330,
        )



    chart_map_1 = [        
            dcc.Graph(figure=fig_map_1,
            animate=True, config=config_plots),
    ]




    row_1 = html.Div(
        [
            dbc.Row(
                [
                    dbc.Card(
                        dbc.Row([
                            dbc.Col(
                                daq.Gauge(
                                    id='my-gauge-app1-1',
                                    #showCurrentValue=True,
                                    color={
                                        "gradient": True,
                                        "ranges": {"green": [0, 4], "red": [4, 10]},
                                    },
                                    value=7,
                                    scale={"start": 0, "interval": 1, "labelInterval": 2},
                                    label="Default Gauge",
                                    max=10,
                                    min=0,),
                            className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                            dbc.Col(
                                daq.Gauge(
                                    id='my-gauge-app1-2',
                                    #showCurrentValue=True,
                                    color={
                                        "gradient": True,
                                        "ranges": {"green": [0, 2000], "red": [2000, 10000]},
                                    },
                                    value=7000,
                                    scale={"start": 0, "interval": 500, "labelInterval": 3},
                                    label="Default Gauge",
                                    max=10000,
                                    min=0,),
                            className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                            dbc.Col(
                                daq.Gauge(
                                    id='my-gauge-app1-3',
                                    #showCurrentValue=True,
                                    color={
                                        "gradient": True,
                                        "ranges": {"green": [0, 2000], "red": [2000, 10000]},
                                    },
                                    value=434,
                                    scale={"start": 0, "interval": 500, "labelInterval": 3},
                                    label="Default Gauge",
                                    max=10000,
                                    min=0,),
                                className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                        ]), 
                    className='shadow cards-info'),
                
                    dbc.Card(
                        dbc.Row([
                            dbc.Col(
                                daq.Gauge(
                                    id='my-gauge-app1-4',
                                    #showCurrentValue=True,
                                    color={
                                        "gradient": True,
                                        "ranges": {"blue": [0, 4], "yellow": [4, 10]},
                                    },
                                    value=7,
                                    scale={"start": 0, "interval": 1, "labelInterval": 2},
                                    label="Default Gauge",
                                    max=10,
                                    min=0,),
                            className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                            dbc.Col(
                                daq.Gauge(
                                    id='my-gauge-app1-5',
                                    #showCurrentValue=True,
                                    color={
                                        "gradient": True,
                                        "ranges": {"blue": [0, 2000], "yellow": [2000, 10000]},
                                    },
                                    value=7000,
                                    scale={"start": 0, "interval": 500, "labelInterval": 3},
                                    label="Default Gauge",
                                    max=10000,
                                    min=0,),
                            className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                            dbc.Col(
                                daq.Gauge(
                                    id='my-gauge-app1-6',
                                    #showCurrentValue=True,
                                    color={
                                        "gradient": True,
                                        "ranges": {"blue": [0, 2000], "yellow": [2000, 10000]},
                                    },
                                    value=434,
                                    scale={"start": 0, "interval": 500, "labelInterval": 3},
                                    label="Default Gauge",
                                    max=10000,
                                    min=0,),
                                className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                        ]),
                    className='shadow cards-info'),

                    dbc.Card(
                            dbc.Row([
                                dbc.Col(
                                    daq.Tank(
                                        id='my-tank-1',
                                        value=5,
                                        min=0,
                                        max=10,
                                    ),
                                className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                                dbc.Col(
                                    daq.Tank(
                                        id='my-tank-2',
                                        value=2,
                                        min=0,
                                        max=10,
                                    ),
                                className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                                dbc.Col(
                                    daq.Tank(
                                        id='my-tank-3',
                                        value=9,
                                        min=0,
                                        max=10,
                                    ),
                                    className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                            ]),
                    className='shadow cards-info'),


                    dbc.Card(chart_line_1,className='shadow cards-info'),
                
                ],
            ),
        ]
    )



    row_2 = html.Div(
        [
            dbc.Row(
                [
                    dbc.Card(
                        dbc.Row([
                            dbc.Col(
                                daq.GraduatedBar(
                                    id="row_2my-graduatedbar-1",
                                    color={"gradient":True,"ranges":{"green":[0,4],"yellow":[4,7],"red":[7,10]}},
                                    showCurrentValue=True,
                                    value=7.5,
                                ),
                            className='col-lg-12 col-md-12 col-sm-12 col-xs-12 col-12'),
                        ]), 
                    className='shadow cards-info'),
                
                    dbc.Card(
                        dbc.Row([
                            dbc.Col(
                                daq.Gauge(
                                    id='row_2my-gauge-app1-4',
                                    #showCurrentValue=True,
                                    color={
                                        "gradient": True,
                                        "ranges": {"orange": [0, 4], "green": [4, 10]},
                                    },
                                    value=7,
                                    scale={"start": 0, "interval": 1, "labelInterval": 2},
                                    label="Default Gauge",
                                    max=10,
                                    min=0,),
                            className='col-lg-6 col-md-6 col-sm-12 col-xs-12 col-12'),
                            dbc.Col(
                                daq.Gauge(
                                    id='row_2my-gauge-app1-5',
                                    #showCurrentValue=True,
                                    color={
                                        "gradient": True,
                                        "ranges": {"orange": [0, 2000], "green": [2000, 10000]},
                                    },
                                    value=7000,
                                    scale={"start": 0, "interval": 500, "labelInterval": 3},
                                    label="Default Gauge",
                                    max=10000,
                                    min=0,),
                            className='col-lg-6 col-md-6 col-sm-12 col-xs-12 col-12'),
                        ]),
                    className='shadow cards-info'),

                    dbc.Card(chart_line_1,className='shadow cards-info'),

                    dbc.Card(chart_sunburst_1,className='shadow cards-info'),

                    dbc.Card(chart_bar_1,className='shadow cards-info'),
                
                ],
            ),
        ]
    )





    row_3 = html.Div(
        [
            dbc.Row(
                [
                    dbc.Card(chart_bubble_1,className='shadow cards-info'),
                
                    dbc.Card(chart_lines_2,className='shadow cards-info'),

                    dbc.Card(chart_lines_3,className='shadow cards-info'),
                    

                    dbc.Card(
                            dbc.Row([
                                dbc.Col(
                                    daq.Tank(
                                        id='row_3my-tank-1',
                                        value=5,
                                        min=0,
                                        max=10,
                                    ),
                                className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                                dbc.Col(
                                    daq.Tank(
                                        id='row_3my-tank-2',
                                        value=2,
                                        min=0,
                                        max=10,
                                    ),
                                className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                                dbc.Col(
                                    daq.Tank(
                                        id='row_3my-tank-3',
                                        value=9,
                                        min=0,
                                        max=10,
                                    ),
                                    className='col-lg-4 col-md-4 col-sm-12 col-xs-12 col-12'),
                            ]),
                    className='shadow cards-info'),

                ],
            ),
        ]
    )





    row_4 = html.Div(
        [
            dbc.Row(
                [
                    dbc.Card(chart_map_1,className='shadow cards-info'),
                
                    dbc.Card(chart_map_1,className='shadow cards-info'),

                ],
            ),
        ]
    )






    return html.Div([html.Div([row_1,row_2,row_3,row_4])])


def layout(clean_data):
    """
    Build the html layout of the first tab.

    This function uses :func:`_charts` and :func:`_app_content` to fill the
    layout of the tab using Dash application components.

    Parameters
    ----------
    clean_data : dict of {str : int or pd.DataFrame}
        Dictionary that contains integers and pd.DataFrames to use as
        data in the charts.

    Returns
    -------
    dash_html_components.html
        Html component composed of charts.
    """
    return app_content(charts(clean_data), clean_data)