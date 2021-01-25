# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:05:18 2021

@author: 4Null
"""
import os
import json
import time
import NTCONST
import requests
import numpy as np

parameters = ["char","charlvl","crown","health","kills","lasthit","level","loops","mutations","skin","type","ultra","wepA","wepB","win","world"]
#timestamp,char,charlvl,crown,health,kills,lasthit,level,loops,mutations,
#skin,type,ultra,wepA,wepB,win,world	

def API_get():
	jsonFormat = requests.get(NTCONST.getStreamlink()).json()
	return jsonFormat,jsonFormat["current"],jsonFormat["previous"]

def update_runs(jsonFormat,currentRun,previousRun):
    """
    Input: jsonFormat,currentRun,previousRun --> the API outputs
    Output: None
    Saves the runs currently diplayed by the nt API to the json file.
    If the API displays a run that has previously been saved it overwrites it with the more recent version of the run.
    Individual runs are identified by their timestamps.
    """        
    with open("output/history.json","r") as jsonfile:
        history_dict = json.load(jsonfile)
        if bool (currentRun):
            history_dict[str(currentRun["timestamp"])] = {_ : str(currentRun[_]) for _ in parameters}
        elif bool(previousRun):
            history_dict[str(previousRun["timestamp"])] = {_ : str(previousRun[_]) for _ in parameters}

    with open("output/history.json","w") as jsonfile:
        json.dump(history_dict,jsonfile)

def continuous_update(interval):
    """
    Input: interval (interval between updates)
    Output: None
    Fetches the current API output saves it to history.json
    and puts the API output to the console 
    """
    current_run_ts = None #current run timestamp
    loop_condition = True
    while loop_condition:
        time.sleep(interval) #aktualisiert alle {interval} sekunden
        
        jsonFormat,currentRun,previousRun = API_get() #gets current API output
        update_runs(jsonFormat,currentRun,previousRun) #history.json update
            
        key="current"
        if not bool(currentRun):
            key="previous"
        if :
            os.system("cls") #clear console output before writing again
            print("World:\t\t" + NTCONST.getWorld(jsonFormat[key]["world"]) + " - " + str(jsonFormat[key]["level"]))
            print("Character:\t" + NTCONST.getCharacter(jsonFormat[key]["char"]) + " Lv: " + str(jsonFormat[key]["charlvl"]))
            print("Weapons:\t" + NTCONST.getGuns(jsonFormat[key]["wepA"]) + " - " + NTCONST.getGuns(jsonFormat[key]["wepB"]))
            print("Crown:\t\t" + NTCONST.getCrown(jsonFormat[key]["crown"]))
            print("Loop:\t\tL" + str(jsonFormat[key]["loops"]))
            print("Kills:\t\t" + str(jsonFormat[key]["kills"]))

            if bool(currentRun) and bool(previousRun) and current_run_ts != currentRun["timestamp"]:
                print("Killed by:\t" + str(NTCONST.getLastHitEnemy(jsonFormat["previous"]["lasthit"])))
                current_run_ts = currentRun["timestamp"]
            else:
                print("Last hit:\t" + NTCONST.getLastHitEnemy(jsonFormat[key]["lasthit"]))
				
		elif not bool(jsonFormat[key]): #if there is no current or previous run
			print("No current or previous run detected!")
	

current_run_ts = None #current run timestamp for returning function
def return_api_str():
    """
    Input: None
    Output: the current CONVERTED! API output, so the actual string like "Crown of Guns"
    [world, character, character_level, weapon_A, waepon_B, crown, loops, kills]
    or if no run is currently displayed by the API
    [None,None,None,None,None,None,None,None] 
    """
	jsonFormat,currentRun,previousRun = API_get() #gets current API output
	update_runs(jsonFormat,currentRun,previousRun) #history.json update
	
	if not bool (currentRun) and not bool (previousRun):
		print("No current or previous run detected!")
		#loop_condition=False #koennte man machen

		
	key="current" #gives out the current run
	if not bool(currentRun):
		key="previous" #or if there is no current run, the previous run
	if bool(jsonFormat[key]):
		return [NTCONST.getWorld(jsonFormat[key]["world"]),	    #world
		        NTCONST.getCharacter(jsonFormat[key]['char']),  #character 
                jsonFormat[key]['charlvl'],                     #character level
                NTCONST.getGuns(jsonFormat[key]["wepA"]),       #weapon A
                NTCONST.getGuns(jsonFormat[key]["wepB"]),       #waepon B
                NTCONST.getCrown(jsonFormat[key]["crown"]),     #crown
                jsonFormat[key]["loops"],                       #loops
                jsonFormat[key]["kills"]]                       #kill count
	elif not bool(jsonFormat[key]): #if there is no current or previous run
		return [None for _ in range(8)]
		
				
if __name__ == "__main__":
#macht dass das folgende nur ausgefuehrt wird wenn die.py direkt ausgefuehrt wird
#so kann man z.B. API_get woanders importieren
    if not os.path.exists("output/history.json"):
        with open("output/history.json", 'x') as jsonfile: pass #if file does not exist, create file
        
    if os.path.getsize("output/history.json") == 0: #if file is empty, dump current run to file
        with open("output/history.json","w") as jsonfile:
            json.dump({},jsonfile)

    continuous_update(5) #update every five seconds