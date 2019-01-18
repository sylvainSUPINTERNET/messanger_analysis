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


"""
Return answers message
"""


def answersTheMost(jsonMsgData):
    totalMessages = getMessages(jsonMsgData)
    limit = len(getMessages(jsonMsgData))

    participants = getParticipantsName(jsonMsgData)
    responseCount = []

    for index, message in enumerate(totalMessages):
        j = index + 1
        if j >= limit:
            print("stop return here")
        else:
            responseCount.append(message["timestamp_ms"] - (totalMessages[j]["timestamp_ms"]))

    return responseCount


"""
Read dictionnary file (default : exemple_words.json)
"""


def getDictionnaireWords(dictionnary='./exemple_words.json'):
    with open(dictionnary) as words:
        dico = json.load(words)
    return dico;


"""
Return most used words
"""


def mostUsedWords(jsonMsgData, dictionnary='./exemple_words.json'):
    countWords = {}

    with open(dictionnary) as words:
        dico = json.load(words)

    # init words
    for word in dico:
        countWords[word] = 0

    for message in getMessages(jsonMsgData):
        for wordSentence in message["content"].split():
            for index, wordDico in enumerate(countWords):
                if wordDico == wordSentence:
                    countWords[wordDico] += 1

    return countWords
