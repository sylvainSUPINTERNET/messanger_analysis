import src.messageService as MessageService
import src.graphService as GraphService

from pprint import pprint
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go

import plotly.graph_objs

# N = 500
# random_x = np.linspace(0, 1, N)
# random_y = np.random.randn(N)

# Create a trace
# trace = go.Scatter(
#   x = random_x,
#  y = random_y
# )

# plotly.offline.plot({
# "data": [
#  plotly.graph_objs.Bar(x=['test1', 'test2', 'test3'], y=[3.4, 4.2, 4.3]),
# ]
# })


# Messages from message as JSON format
jsonData = MessageService.parseMessage('message_umber.json')

# Global infos about the conversation group
infos_title = MessageService.getTitle(jsonData)
infos_thread = MessageService.getThreadType(jsonData)
infos_still_participants = MessageService.isStillParticipants(jsonData);
if (infos_still_participants):
    infos_still_participants = "group active"
else:
    infos_still_participants = "group non active"

# Participants of conversation (list of names)
pariticpans = MessageService.getParticipantsName(jsonData)



print("_____ MOST CHARACTER WRITTEN SCORE ____")
print("")
pprint(MessageService.mostCharacterWritten(jsonData))
print("_______________________________")

print("_____ MOST MESSAGE SEND ____")
print("")
pprint(MessageService.mostMessageSend(jsonData))
print("_______________________________")






# with open('message_neungruetai.json') as message:
#   data = json.load(message)

# pprint(data)
# pprint(data["messages"])
