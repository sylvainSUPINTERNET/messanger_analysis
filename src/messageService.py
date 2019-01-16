import src.utils as Utils
import json
from pprint import pprint

import numpy as np

"""
Parse messanger message format JSON
"""


def parseMessage(filename):
    with open(filename) as messages:
        data = json.load(messages)
        # print(data)
        return data


def getMessages(jsonMsgData):
    return jsonMsgData["messages"]


"""
Return title of group messanger (if exist)
"""


def getTitle(jsonMsgData):
    return jsonMsgData["title"]


"""
Return type of thread messanger (if exist)
"""


def getThreadType(jsonMsgData):
    return jsonMsgData["thread_type"]


"""
Return boolean - true if still participants in group // false
"""


def isStillParticipants(jsonMsgData):
    return jsonMsgData["is_still_participant"]


"""
Parse conversation participants
"""


def getParticipantsName(jsonMsgData):
    arr_participant = []
    for participant in jsonMsgData["participants"]:
        arr_participant.append(participant["name"])
    return arr_participant


"""
Return sort array of the users with the most characters written in the group (sort DESC)
"""


def mostCharacterWritten(jsonMsgData):
    participants = getParticipantsName(jsonMsgData)
    score = {}

    # init score
    for name in participants:
        score[name] = 0

    for message in getMessages(jsonMsgData):
        score[message["sender_name"]] += len(message["content"])

    return Utils.sortDictDesc(score)


"""
Return most messages send DESC (score)
"""


def mostMessageSend(jsonMsgData):
    participants = getParticipantsName(jsonMsgData)
    score = {}

    # init score
    for name in participants:
        score[name] = 0

    for message in getMessages(jsonMsgData):
        score[message["sender_name"]] += 1

    return Utils.sortDictDesc(score)

"""
Return biggest pave DESC (score)
"""


def getBiggestPave(jsonMsgData):
    return "todo"

# TODO
# Courbe de frequence de messages
# Courbe de temps entre chaque message
