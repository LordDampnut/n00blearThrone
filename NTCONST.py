# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:12:53 2021

@author: 4Null
"""
import numpy

enemies = numpy.loadtxt("enemies.txt", delimiter="\t", dtype=str)
world = numpy.loadtxt("worlds.txt", delimiter="\t", dtype=str)
crown = numpy.loadtxt("crowns.txt", delimiter="\t", dtype=str)
guns = numpy.loadtxt("guns.txt", delimiter="\t", dtype=str)
mutations = numpy.loadtxt("mutations.txt", delimiter="\t", dtype=str)
#level
#health
#kills
#loops
#skin (0,1)
#ultra
#


character = ["","Fish", "Crystal", "Eyes", "Melting", "Plant", "Y.V.", "Steroids",
       "Robot", "Chicken", "Rebel", "Horror", "Rogue", "Skeleton", "Frog"]

i = 0

def getCharacter(n):
    return character[n]

def getLastHitEnemy(n):
    return enemies[n+1][1]

def getWorld(n):
    i = numpy.where(world == str(n))
    #i = world[0].index(str(n))
    return world[i][0]

def getCrown(n):
    return crown[n-1][1]

def getGuns(n):
    return guns[n][1]