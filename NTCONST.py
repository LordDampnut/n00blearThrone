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
