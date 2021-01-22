# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:05:18 2021

@author: 4Null
"""
import os
import NTCONST
import requests
import numpy as np

def recordRun(): #write previous run to file, csv format
    
    time = np.loadtxt("output/history.txt", delimiter=",", dtype=str)
    if os.stat("output/history.txt").st_size==0 or not (previousRun["timestamp"] == int(time.T[0][-1])): #os.stat("output/history.txt").st_size==0 falls das history file leer ist
        file = open("output/history.txt","a")
        
        variables = ["timestamp","char","charlvl","crown","health","kills","lasthit","level","loops","mutations","skin","type","ultra","wepA","wepB","win","world"]
        write_string = ",".join([str(previousRun[_]) for _ in variables])
        file.write("\n"+ write_string)

        #timestamp,char,charlvl,crown,health,kills,lasthit,level,loops,mutations,
        #skin,type,ultra,wepA,wepB,win,world
        file.close()


jsonFormat = requests.get(NTCONST.getStreamlink()).json()


currentRun = jsonFormat["current"]
previousRun = jsonFormat["previous"]

if  bool (currentRun):
    key = "current"
    #print("Hello World")
elif bool (previousRun):
    key = "previous"
    #print("Hah noob")
else:
    #print("No current or previous run detected!")
    exit()  

print("World:\t\t" + NTCONST.getWorld(jsonFormat[key]["world"]) + " - " + 
      str(jsonFormat[key]["level"]))
print("Chacacter:\t" + NTCONST.getCharacter(jsonFormat[key]["char"]) +
  " Lv: " + str(jsonFormat[key]["charlvl"]))

print("Weapons:\t" + NTCONST.getGuns(jsonFormat[key]["wepA"]) + " - " + 
      NTCONST.getGuns(jsonFormat[key]["wepB"]))

print("Crown:\t\t" + NTCONST.getCrown(jsonFormat[key]["crown"]))

print("Loop:\t\tL" + str(jsonFormat[key]["loops"]))

if jsonFormat[key]["health"] == 0:
    print("Killed by:\t" + str(NTCONST.getLastHitEnemy(jsonFormat[key]["lasthit"])))
    recordRun() #hah you died
else:
    print("Last hit:\t" + NTCONST.getLastHitEnemy(jsonFormat[key]["lasthit"]))
    
print("Kills:\t\t" + str(jsonFormat[key]["kills"]))
