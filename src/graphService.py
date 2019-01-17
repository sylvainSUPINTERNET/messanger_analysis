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
    return plotly.offline.plot(fig, filename="charts/amount_message_by_participants")


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

    plotly.offline.plot(fig, filename='charts/most_characters_written')


"""
Draw radar - biggest pave written
"""


def drawBiggestPave(jsonMsgData):
    labels = []
    values = []
    for message in MessageService.getBiggestPave(jsonMsgData):
        labels.append(message[0])
        values.append(message[1])

    trace = go.Pie(labels=labels, values=values, title="Biggest Pavé")

    return plotly.offline.plot([trace], filename="charts/biggest_pave")


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
    plotly.offline.plot(fig, filename='charts/time_curve_between_each_messages')

