# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:12:53 2021

@author: 4Null
"""
import numpy as np

# import die

enemies = np.loadtxt("enemies.txt", delimiter="\t", dtype=str)
world = np.loadtxt("worlds.txt", delimiter="\t", dtype=str)
crown = np.loadtxt("crowns.txt", delimiter="\t", dtype=str)
guns = np.loadtxt("guns.txt", delimiter="\t", dtype=str)
mutations = np.loadtxt("mutations.txt", delimiter="\t", dtype=str)

# level
# health
# kills
# loops
# skin (0,1)
# ultra
#
# print(f"Length of s1 = {len(s1)}")
templist = [0] * 29  #
mutationliterals, counter = [], []  #
mutationsstring = ""


# 00000101000100000100000000010
def getmutationstring():
    return mutationsstring

def setmutationstring(temp):
    mutationsstring = temp

def getmutdiff(newstring, oldstring=templist):
    """
    Function returns a list containing 0 and 1 where every "1" is the difference between the input and output strings
    :param oldstring: "old" mutation string containing 0 and 1
    :param newstring: "new" mutation string containing 0 and 1
    """
    """
    Newstring coming in, vergleiche mit altem string. (Templist) 
    Wenn gleich dann hat sich nix geaendert. return 0es (neue variable?)
    
    """
    if newstring == oldstring: return templist  # wenn keine aenderungen dann alten wert zurueck geben

    listold, listnew, difference = list(oldstring), list(newstring), []
    for _ in range(len(listold)):
        j = (int(listold[_]) ^ int(listnew[_]))
        print(j)
        difference.append(
            (int(listold[_]) ^ int(listnew[_])))  # xor both strings position for position and append result to output list
    templist = newstring
    # print(f"Differenz: {difference}")

    return sortMutation(difference)


def sortMutation(differencestr):
    temp = getmutationstring()

    for i in range(len(differencestr)):
        temp += mutations[i][1]
    return temp



"""
def getsortedmutation(omt, nmt):  # old mutation string, new mutation string
    print(int(omt))  # debug
    if int(nmt) < int(omt):
        tmeplist = []
        return templist
        print("scheisse")
    elif (int(nmt) == int(omt)):
        return templist

    if int(nmt) == 0:  # wenn alte mutation alle 0 dann sortierte liste zurücksetzen
        global sortedmutation
    else:
        global sortedmutation
        sortedmutation = templist

    changed = []  # leere output liste erstellen
    list1, list2 = list(omt), list(nmt)  # strings in listen umwandeln

    for i in range(len(list1)):  # len = 29
        xorresult = (int(list1[i]) ^ int(list2[i]))
        print(xorresult)
        if xorresult == 1:
            print(mutations[xorresult][1])
            templist.append(mutations[xorresult][1])

    return templist

    return ','.join(map(str, sortedmutation))
"""


def getStreamlink():
    return str(np.loadtxt("streamlink.txt", dtype=str))


character = ["", "Fish", "Crystal", "Eyes", "Melting", "Plant", "Y.V.", "Steroids",
             "Robot", "Chicken", "Rebel", "Horror", "Rogue", "Skeleton", "Frog"]


def getCharacter(n):
    return character[n]


def getLastHitEnemy(n):
    return enemies[n + 1][1]


def getWorld(n):
    i = np.where(world == str(n))
    # i = world[0].index(str(n))
    return world[i][0]


def getCrown(n):
    return crown[n - 1][1]


def getGuns(n):
    return guns[n][1]


def writelink(streamlink):
    file = open("streamlink.txt", "w")
    file.write(streamlink)


if __name__ == "__main__":
    print(templist)
    # getmutdiff("00000000000000000000000000010")  # used for testing
    # getmutdiff("00000000000000000100000000010")
