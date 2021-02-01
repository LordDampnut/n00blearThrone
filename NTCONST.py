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

# level
# health
# kills
# loops
# skin (0,1)
# ultra
#
# templist = [0] * 29
mutationliterals, refmutations = [], [0] * 29  #


def checksumoflist(l):
    """
    sums up all values of a list (consisting of 0 and 1)
    :param l: list of mutations containing 0 and 1
    """
    x = 0
    for _ in range(len(l)):
        x += int(l[_])
    return x


def getmutationliterals(mutationstring):
    """
    returns literals of mutations as sorted list with respect to time of acquirence
    does only work when the script was running before the game started.

    :param mutationstring: Mutationstring as it is generated by the game
    """
    global refmutations
    global mutationliterals
    if checksumoflist(mutationstring) < checksumoflist(refmutations):  # check if run ended if zes, delete old data
        mutationliterals, refmutations = [], [0] * 29  # reset values
    if not checksumoflist(mutationstring) == checksumoflist(refmutations):
        diffstring = getmutdiff(mutationstring)  # a string where change is indicated by a "1" (index)
        for _ in range(len(diffstring)):
            if int(diffstring[_]) == 1:
                mutationliterals.append(mutations[_][1])
    refmutations = list(mutationstring)

    return mutationliterals


def getmutdiff(newstring):
    """
    Function returns a list containing 0 and 1 where every "1" is the difference between the input and output strings
    :param oldstring: "old" mutation string containing 0 and 1
    :param newstring: "new" mutation string containing 0 and 1
    """

    global refmutations
    listold, listnew, difference = list(refmutations), list(newstring), []
    for _ in range(len(listold)):
        difference.append(
            (int(listold[_]) ^ int(
                listnew[_])))  # xor both strings position for position and append result to output list
    return difference


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
