# n00blearThrone
Description

nooblearThrone is a WIP tool to track you failing ingame.
Everytime you die an entry in the logfile is created.
After many horrible deaths to maggots or little hunter this file can then be used to create a statistic how much you suck with each character, weapon and mutation.
If you then interpret the data you probably wont suck less at playing the game.

Info about the stream key has been taken from [NT Fandom Wiki](https://nuclear-throne.fandom.com/wiki/Stream_Keys)

# ToDo
* Finish NTCONST and add all "decoders" for the json string
  * find a way to display the speacial worlds on the console (e.g. world 102 as Pizza sewers)
* reformat console output to f-string and add more values
* stream key from file so the user doesnt have to edit the .py file
* convert character variable from hardcoded list to file and read the file
* Add retrun value if streamlink.txt is empty to NTCONST.getStreamlink()
* and more!


## ToDo (maybe)
* Add GUI with live update
* add evaluation of logfile in python, so the user doesnt have to use excel or similar
* Discord Bot implementation - statistics, user averages, recent run info, run shaming and more!
