import src.utils as Utils
import json
from pprint import pprint
import numpy as np

"""
Parse messanger message format JSON
"""


def parseMessage(filename="message_umber.json"):
    with open(filename) as messages:
        data = json.load(messages)
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
    participants = getParticipantsName(jsonMsgData)
    score = {}

    # init score
    for name in participants:
        score[name] = 0

    for message in getMessages(jsonMsgData):
        score[message["sender_name"]] = Utils.compare(score[message["sender_name"]], len(message["content"]))

    return Utils.sortDictDesc(score)


# bon ca A VOIR
"""
Return dictionnary -> time between 2 messages (message 1 - timestamp : message 2 - timestamp, message 2 ....)
"""


def calculResponseTimeBetween2Messages(jsonMsgData):
    response_times = {}
    messages_size_limit = len(jsonMsgData["messages"]) - 1
    for index, message in enumerate(getMessages(jsonMsgData)):
        if index < messages_size_limit:
            print(message["content"])
            print("__________________________________________")
            print(getMessages(jsonMsgData)[index + 1]["content"])

            response_times["msg_" + index.__str__()] = [message["timestamp_ms"],
                                                        getMessages(jsonMsgData)[index + 1]["timestamp_ms"]]

        # print(message["timestamp_ms"])  # timestamp msg1
        # print(getMessages(jsonMsgData)[index + 1]["timestamp_ms"])  # response timestamp to msg1
        # print("ok")
        # go 2 by 2 ...
    pprint(response_times)


"""
Return time curve between each messages
"""


def timeBetweenEachMessages(jsonMsgData, default=True):
    timecurve = []
    totalMessages = getMessages(jsonMsgData)

    for index, message in enumerate(totalMessages):
        if index < len(totalMessages) - 1:
            timecurve.append(message["timestamp_ms"] - totalMessages[index + 1]["timestamp_ms"])

    if default:
        # return timecurve as Default json format (lastest first > oldest last)
        return timecurve
    else:
        # return timecurve reversed (oldest to lastest)
        reversed = timecurve[::-1]
        return reversed
