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


"""
Draw radar - most characters written
"""


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
Draw radar - biggest pave written
"""


def drawBiggestPave(jsonMsgData):
    labels = []
    values = []
    for message in MessageService.getBiggestPave(jsonMsgData):
        labels.append(message[0])
        values.append(message[1])

    trace = go.Pie(labels=labels, values=values)

    return plotly.offline.plot([trace], filename="dist/biggest_pave")


"""
Draw time curve between each messages
"""


def drawTimeCurveBetweenEachMessages(jsonMsgData):
    timesBetweenMessages = MessageService.timeBetweenEachMessages(jsonMsgData, True)

    # spacing (x)
    random_x = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000]

    random_y0 = timesBetweenMessages
    # random_y1 = [9, 2, 3, 4, 5, 6]
    # random_y2 = [3, 8, 10, 4, 5, 6]

    # Create traces
    trace0 = go.Scatter(
        x=random_x,
        y=random_y0,
        mode='lines',
        name='lines'
    )



    data = [trace0]

    layout = go.Layout(
        title='Curve time between each messages (ms)',
        xaxis=dict(
            title='x ms',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='y ms',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='time_curve_between_each_messages')


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
