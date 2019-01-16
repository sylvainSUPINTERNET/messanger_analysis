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


print("")
print("")
print(" EXPORT DU :", MessageService.getPeriod(jsonData))
print("")
print("")
print("_____ MOST CHARACTER WRITTEN SCORE ____")
print("")
pprint(MessageService.mostCharacterWritten(jsonData))
print("_______________________________")
print("")
print("```````````````````````````````````````")
print("```````````````````````````````````````")
print("_____ MOST MESSAGE SEND ____")
print("")
pprint(MessageService.mostMessageSend(jsonData))
print("_______________________________")
print("")
print("```````````````````````````````````````")
print("```````````````````````````````````````")
print("_____ BIGGEST PAVE SEND ____")
print("")
pprint(MessageService.getBiggestPave(jsonData))
print("_______________________________")



MessageService.calculResponseTimeBetween2Messages(jsonData);

# TODO histogramme en %  des stats simple genre most messages sended / characters wirtten etc
# TODO curve mias avant calculer le response time / frequency
#GraphService.timeBetweenMessages(jsonData)
#GraphService.curveCompareFrequencyAndResponseTime(jsonData)



# dans la doc parler que le message_umber contient uen clef custom a rajouter si on veut tester avec son propre messanger