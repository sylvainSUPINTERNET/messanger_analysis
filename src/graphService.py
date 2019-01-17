import src.messageService as MessageService
import src.utils as Utils
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.graph_objs

import numpy as np

from pprint import pprint

"""
Draw radar - amount of message by participants
"""


def drawRadarAmountOfMessageByParticipants(jsonMsgData):
    r = []
    theta = []
    for message in MessageService.mostMessageSend(jsonMsgData):
        theta.append(message[0])
        r.append(message[1])

    data = [go.Scatterpolar(
        r=r,
        theta=theta,
        fill='toself'
    )]

    layout = go.Layout(
        title='Amount of message by participants',
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 20]
            )
        ),
        showlegend=False
    )

    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig, filename="dist/amount_message_by_participants")


def drawMostCharactersWritten(jsonMsgData):
    x = []
    y = []

    for message in MessageService.mostCharacterWritten(jsonMsgData):
        x.append(message[0])
        y.append(message[1])

    data = [go.Bar(
        x=x,
        y=y
    )]

    layout = go.Layout(
        title='Most characters written')

    fig = go.Figure(data=data, layout=layout)

    plotly.offline.plot(fig, filename='dist/most_characters_written')


"""
Draw curve - compare frequency / response time
"""


def curveCompareFrequencyAndResponseTime(jsonMsgData):
    messages_dates = []  # abscissee (axe x)

    for message in jsonMsgData["messages"]:
        messages_dates.append(Utils.convertMsInDatetime(message["timestamp_ms"]))

    y = [00, 10, 20, 30, 40, 50, 60, 70, 80, 90]  # y

    freq = go.Scatter(
        x=messages_dates,
        y=y,
        name='Frequency'
    )
    resT = go.Scatter(
        x=messages_dates,
        y=y,
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
            title='y %',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = plotly.offline.plot(fig, filename='dist/frequency_responseTime_messages_stats')
    return "rate TODO"

# todo http://lablanchisserie.fr/extern-links/iim/python/Projet%20de%20la%20semaine%20data%20science.pdf


# TODO
# draw en x (nom des participants et en y unit) les truck genre nombre de message etc
