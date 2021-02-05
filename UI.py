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
import die
import diagnostics as diag


class InfoPanel:
    def __init__(self, parent):
        self.Maxhealth = 0
        self.InfoPanel = tk.Frame(parent, padx=5, pady=5)
        self.death_probs =diag.get_from_history('death_probabilities')

        
        self.CharLabel = tk.Label(self.InfoPanel, text="Character: ")
        self.HealthLabel = tk.Label(self.InfoPanel, text="Health: ")
        self.LevelLabel = tk.Label(self.InfoPanel, text="Level:")
        self.GunLabel = tk.Label(self.InfoPanel, text="Guns: ")
        self.WorldLabel = tk.Label(self.InfoPanel, text="World: 0-0 L0")
        self.EnemyLabel = tk.Label(self.InfoPanel, text="Last hit by: ")
        self.CrownLabel = tk.Label(self.InfoPanel, text="Crown: ")
        self.KillLabel = tk.Label(self.InfoPanel, text="Kills: ")
        self.MutationLabel = tk.Label(self.InfoPanel, text="Mutations: ")
        self.DeathPanel = tk.Label(self.InfoPanel, text="Probability of Death in this level: low but never zero")
        self.InfoPanel.grid()

        self.CharLabel.grid()
        self.HealthLabel.grid()
        self.LevelLabel.grid()
        self.GunLabel.grid()
        self.WorldLabel.grid()
        self.EnemyLabel.grid()
        self.CrownLabel.grid()
        self.KillLabel.grid()
        self.MutationLabel.grid(column=3, row=0, padx=5)
        self.DeathPanel.grid()
        
        self.InfoPanel.after(1000, self.refresh_InfoPanel)

    def refresh_InfoPanel(self):
        self.char, self.charlvl, self.crown, self.health, self.kills, self.lasthit, self.level, self.loops, self.mutations, \
        self.skin, self.type, self.ultra, self.gun1, self.gun2, self.win, self.world = die.return_api_str()

        # "char", "charlvl", "crown", "health", "kills", "lasthit", "level", "loops", "mutations", "skin", "type",
        # "ultra", "wepA", "wepB", "win", "world"

        # Debug to see if thing actually loaded

        """
        if self.world:
            # os.system("cls")
            print("Check")
        """

        # set max health according to characters
        if self.char == 2:
            self.Maxhealth = 10
            if self.ultra == 1:  # might change to "2" dunno yet
                self.Maxhealth += 6
        elif self.char == 4:
            self.Maxhealth = 2
        elif self.char == 13:
            self.Maxhealth = 6
        else:
            self.Maxhealth = 8

        if list(self.mutations)[1] == "1":
            self.Maxhealth += 4  # Add 4 to maxhealth if Rhino Skin was choosen
            # print(self.Maxhealth)
        # assemble health string
        if (self.health is not None):
            self.health = "%s / %i" % (self.health, self.Maxhealth)

        # Skin
        if (self.skin):
            self.skin = 'B'
        else:
            self.skin = 'A'

        # Worldstring
        if (self.world is not None and self.level is not None and self.loops is not None):
            self.worldstring = "World: %s - %i L%i" % (NTCONST.worldliterals(self.world), self.level, self.loops)

        # update all the labels
        self.CharLabel.configure(text="Character: " + NTCONST.getCharacter(self.char) + " " + self.skin + "-Skin")
        self.HealthLabel.configure(text="Health: " + self.health)
        self.LevelLabel.configure(text="Level: %i" % self.charlvl)
        self.GunLabel.configure(text="Guns: " + NTCONST.getGuns(self.gun1) + ", " + NTCONST.getGuns(self.gun2))
        self.WorldLabel.configure(text=self.worldstring)
        self.EnemyLabel.configure(text="Last hit by: " + NTCONST.getLastHitEnemy(self.lasthit))
        self.CrownLabel.configure(text="Crown: " + NTCONST.getCrown(self.crown))
        self.KillLabel.configure(text="Kills: %i" % self.kills)
        self.MutationLabel.configure(
            text="Mutations: %s\n" % NTCONST.formatliterals(NTCONST.getmutationliterals(self.mutations)))
        current_death_prob = self.death_probs[f"{self.world}-{self.level}-{self.loops}"] 
        self.DeathPanel.configure(text=f" Death probabllity: {(current_death_prob*100):.1f} %" )


        self.InfoPanel.after(1000, self.refresh_InfoPanel)


if __name__ == "__main__":
    # variables from other places

    # https://tb-api.xyz/stream/get?s=76561198126315242&key=GHMNSTZ64

    # API link from file
    apilink = NTCONST.getStreamlink()
    """
    print(apilink)
    #If link is empty, open window to insert SteamID and StreamKey
    if apilink == 0 :
        functionAPIlink
    else:
    """
    # extract Steam64-ID and Stream Key from API link
    split = apilink.split('=')
    # print(split)
    Streamkey = split[2]
    # print(Streamkey)
    split2 = split[1].split('&')
    SteamID = split2[0]


    # functions

    # Assemble API link from entries in linkChange window and write into file
    def writeStreamlink(IDChangeEntry, KeyChangeEntry, root):
        SteamID = IDChangeEntry.get()
        Streamkey = KeyChangeEntry.get()
        print("Debug: init of writeStreamlink()")
        apilink = "https://tb-api.xyz/stream/get?s=" + SteamID + "&key=" + Streamkey
        print("Debug: Streamlink is " + apilink)
        NTCONST.writelink(apilink)
        root.update()


    def functionAPIlink():
        # make new window to change steam ID and stream key
        linkChange = tk.Toplevel(root)
        linkChange.title("Change API Info")
        linkChange.geometry("300x120")
        linkChange.grab_set()

        # Make Frame for Steam ID
        steamIDframe = tk.Frame(linkChange)
        steamIDframe.pack(padx=5, pady=5)

        # Add content to Steam ID Frame
        IDChangeLabel = tk.Label(steamIDframe, text="Steam-64 ID:")
        IDChangeLabel.pack(side=tk.LEFT)

        IDChangeEntry = tk.Entry(steamIDframe, width=12)
        IDChangeEntry.insert(0, SteamID)
        IDChangeEntry.pack(padx=5, pady=5)

        # Make Frame for Stream Key
        streamKeyFrame = tk.Frame(linkChange)
        streamKeyFrame.pack(padx=5, pady=5)

        # Add content to Stream Key Frame
        KeyChangeLabel = tk.Label(streamKeyFrame, text="Stream Key:")
        KeyChangeLabel.pack(side=tk.LEFT)

        KeyChangeEntry = tk.Entry(streamKeyFrame, width=12)
        KeyChangeEntry.insert(0, Streamkey)
        KeyChangeEntry.pack(padx=5, pady=5)

        linkChangebutton = tk.Button(linkChange, text="Confirm and Close",
                                     command=lambda: [writeStreamlink(IDChangeEntry, KeyChangeEntry, root),
                                                      linkChange.destroy()])
        linkChangebutton.pack()


    ############### MAIN WINDOW #################################
    # make Main window
    root = tk.Tk()
    root.geometry("500x450")
    root.title("N00blear Throne")

    for i in range(4):
        root.columnconfigure(i, weight=1)

    root.rowconfigure(1, weight=1)

    ### ADD UI STUFF HERE ###
    mainframe = tk.Frame(root, width=300, borderwidth=2, relief="groove")

    # Info about SteamID and StreamKey + button to change them
    tk.Label(mainframe, text="Steam ID: " + SteamID).grid(column=1)
    tk.Label(mainframe, text="Stream Key: " + Streamkey).grid(column=1)
    buttonAPIlink = tk.Button(mainframe, text="Change", command=functionAPIlink)
    buttonAPIlink.grid(column=2, padx=5, pady=5)
    mainframe.grid(column=0, columnspan=1, padx=5, pady=5)
    # Info Panel about current run

    InfoPanel = InfoPanel(root)

    # button to close program
    exitbutton = tk.Button(root, text="Close", command=exit)
    exitbutton.grid(column=0, row=2, pady=5, padx=20)

    ############### MAIN WINDOW END ####################

    # loop that shit
    root.mainloop()
# aww yiss
