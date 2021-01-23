# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:05:18 2021

@author: 4Null
"""
import os
import json
import NTCONST
import requests
import numpy as np

parameters = ["char","charlvl","crown","health","kills","lasthit","level","loops","mutations","skin","type","ultra","wepA","wepB","win","world"]
#timestamp,char,charlvl,crown,health,kills,lasthit,level,loops,mutations,
#skin,type,ultra,wepA,wepB,win,world	

def API_get():
	jsonFormat = requests.get(NTCONST.getStreamlink()).json()
	return jsonFormat,jsonFormat["current"],jsonFormat["previous"]

def UpdateRuns():
	"""
	Input: None
	Output: None
	Saves the runs currently diplayed by the nt API to the json file.
	If the API displays a run that has previously been saved it overwrites it with the more recent version of the run.
	Individual runs are identified by their timestamps.
	"""
	jsonFormat,currentRun,previousRun = API_get()
	
    with open("output/history.json","a") as jsonfile:
		history_dict = json.load(jsonfile)
		if bool (currentRun):	
			history_dict[str(previousRun("timestamp"))] = {variable : str(previousRun[_]) for _ in variables}
			
		elif bool (previousRun):
			history_dict[str(currentRun("timestamp"))] = {variable : str(currentRun[_]) for _ in variables}
		json.dump(history_dict,jsonfile)

jsonFormat,currentRun,previousRun = API_get()

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
