import src.messageService as MessageService
import src.graphService as GraphService
from pprint import pprint

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

# Draw graphics
GraphService.drawRadarAmountOfMessageByParticipants(jsonData)
GraphService.drawMostCharactersWritten(jsonData)
GraphService.drawBiggestPave(jsonData)
GraphService.drawTimeCurveBetweenEachMessages(jsonData)
GraphService.drawMostUsedWord(jsonData)
GraphService.drawResponseTimeCurve(jsonData)
