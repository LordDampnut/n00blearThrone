# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:12:53 2021

@author: 4Null
"""
import numpy as np

enemies = np.loadtxt("enemies.txt", delimiter="\t", dtype=str)
world = np.loadtxt("worlds.txt", delimiter="\t", dtype=str)
crown = np.loadtxt("crowns.txt", delimiter="\t", dtype=str)
guns = np.loadtxt("guns.txt", delimiter="\t", dtype=str)
mutations = np.loadtxt("mutations.txt", delimiter="\t", dtype=str)
sortedmutation = []

# level
# health
# kills
# loops
# skin (0,1)
# ultra
#

"""  # Don't use this function yet, it has to be fixed :(
def getsortedmutation(omt, nmt):  # old mutation string, new mutation string
    # Hard Work foes here
    
mutations = np.loadtxt("mutations.txt", delimiter="\t", dtype=str)

# print(f"Length of s1 = {len(s1)}")
list1 = list(s1)
list2 = list(s2)
templist = []
sortedmutation = []
change = []


def getsortedmutation(omt, nmt):  # old mutation string, new mutation string
    print(int(omt))  # debug
    if int(nmt) < int(omt):
        tmeplist = []
        return templist
        print("scheisse")
    elif (int(nmt) == int(omt)):
        return templist

    if int(nmt) == 0: #wenn alte mutation alle 0 dann sortierte liste zurücksetzen
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
