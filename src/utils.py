import numpy as np

def sortDictDesc(dict):
    return sorted(dict.items(), key=lambda kv: kv[1], reverse=True)


def compare(nb1, nb2):
    if(nb1 > nb2):
        return nb1
    if(nb1 < nb2):
        return nb2
    if(nb1 == nb2):
        return nb1

def average(list):
    return np.mean(list)