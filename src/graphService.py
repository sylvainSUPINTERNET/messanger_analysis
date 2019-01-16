import src.messageService as MessageService
import src.utils as Utils
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.graph_objs

import numpy as np

from pprint import pprint

"""
Draw curve - compare frequency / response time
"""


def curveCompareFrequencyAndResponseTime(jsonMsgData):
    messages_dates = []  # abscissee (axe x)

    for message in jsonMsgData["messages"]:
        messages_dates.append(Utils.convertMsInDatetime(message["timestamp_ms"]))

    freq = go.Scatter(
        x=messages_dates,
        y=[1, 2, 3, 4, 5, 6, 7, 8, 9],
        name='Frequency'
    )
    resT = go.Scatter(
        x=messages_dates,
        y=[1, 0, 3, 4, 5, 6, 10, 8, 9],
        name='Reponse time'
    )
    data = [freq, resT]
    layout = go.Layout(
        title='Compaire messages frequency and response time',
        xaxis=dict(
            title='x Datetime',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='y Unit',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = plotly.offline.plot(fig, filename='./dist/frequency_responseTime_messages_stats')
    return "rate TODO"

# todo http://lablanchisserie.fr/extern-links/iim/python/Projet%20de%20la%20semaine%20data%20science.pdf
