# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:29:44 2021

@author: nukecuber
"""
import tkinter as tk
from tkinter import messagebox
import os
import NTCONST
import requests
import numpy as np

#variables from other places

#https://tb-api.xyz/stream/get?s=76561198126315242&key=GHMNSTZ64

#API link from file
apilink = NTCONST.getStreamlink()
"""
print(apilink)
#If link is empty, open window to insert SteamID and StreamKey
if apilink == 0 :
	functionAPIlink
else:
"""
	#extract Steam64-ID and Stream Key from API link
split = apilink.split('=')
	#print(split)
Streamkey = split[2]
	#print(Streamkey)
split2 = split[1].split('&')
SteamID = split2[0]
	#print(SteamID)


#Assemble API link from entries in linkChange window and write into file
def writeStreamlink():
	print("Debug: init of writeStreamlink()")
	apilink = "https://tb-api.xyz/stream/get?s=" + SteamID + "&key=" + Streamkey


#functions
def functionAPIlink():

	#messagebox.showinfo("Hi", "This is where you could change the link if i was any competent lol")
	#make new window
	linkChange = tk.Toplevel(root)
	linkChange.title("Change API Info")
	linkChange.geometry("300x120")
	linkChange.grab_set()

	#Make Frame for Steam ID
	steamIDframe = tk.Frame(linkChange)
	steamIDframe.pack(padx=5, pady=5)

	#Add content to Steam ID Frame
	IDChangeLabel = tk.Label(steamIDframe, text="Steam-64 ID:")
	IDChangeLabel.pack(side = tk.LEFT)

	IDChangeEntry = tk.Entry(steamIDframe, width = 12)
	IDChangeEntry.insert(0, SteamID)
	IDChangeEntry.pack(padx = 5, pady = 5)

	#Make Frame for Stream Key
	streamKeyFrame = tk.Frame(linkChange)
	streamKeyFrame.pack(padx = 5, pady = 5)

	#Add content to Stream Key Frame
	KeyChangeLabel = tk.Label(streamKeyFrame, text="Stream Key:")
	KeyChangeLabel.pack(side=tk.LEFT)

	KeyChangeEntry = tk.Entry(streamKeyFrame, width = 12)
	KeyChangeEntry.insert(0, Streamkey)
	KeyChangeEntry.pack(padx=5, pady=5)

	linkChangebutton = tk.Button(linkChange, text = "Confirm and Close", command = lambda:[writeStreamlink(),linkChange.destroy()])
	linkChangebutton.pack()
	

############### MAIN WINDOW #################################
#make Main window
root = tk.Tk()
root.geometry("500x150")
root.title("Nuclear Throne Thing")
### ADD UI STUFF HERE ###
mainframe = tk.Frame(root, width = 30)
mainframe.pack(padx=5, pady=5)

tk.Label(mainframe, text = "Steam ID: " + SteamID).pack()
tk.Label(mainframe, text = "Stream Key:" + Streamkey).pack()
buttonAPIlink = tk.Button(mainframe, text = "Change", command = functionAPIlink)
buttonAPIlink.pack(side=tk.RIGHT)


#button to close program
exitbutton = tk.Button(root, text ="close", command = exit)
exitbutton.pack()

############### MAIN WINDOW END ####################

#loop that shit
root.mainloop()
#aww yiss