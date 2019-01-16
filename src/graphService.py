import src.messageService as MessageService

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.graph_objs

import numpy as np


N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x=random_x,
    y=random_y
)

plotly.offline.plot({
    "data": [
        plotly.graph_objs.Bar(x=['test1', 'test2', 'test3'], y=[3.4, 4.2, 4.3]),
    ]
})




"""
Draw curve of time between each messages
"""

def timeBetweenMessages(jsonMsgData):
    participants = MessageService.getParticipantsName(jsonMsgData)
    score = {}

    # init score
    for name in participants:
        score[name] = 0

    N = len(score)
    random_x = np.linspace(0, 100)
    random_y = np.random.randn(100)

    # Create a trace
    trace = go.Scatter(
        x=random_x,
        y=random_y
    )

    data = [trace]

    return plotly.offline.plot(data, filename='curve-time-between-messages')

"""
Draw frequence curve for messages
"""
def frequencyMessage(jsonMsgData):

    trace1 = go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[1, 1, 2, 3, 4, 5, 6, 7, 8],
        name='Rate'
    )
    trace2 = go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[1, 0, 3, 2, 5, 4, 7, 6, 8],
        name='Latency'
    )
    data = [trace1, trace2]
    layout = go.Layout(
        title='Compaire messages rate and latency',
        xaxis=dict(
            title='x Days',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='y Times (ms)',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = plotly.offline.plot(fig, filename='styling-names')
    return "rate TODO"




# todo http://lablanchisserie.fr/extern-links/iim/python/Projet%20de%20la%20semaine%20data%20science.pdf