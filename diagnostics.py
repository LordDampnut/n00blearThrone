import numpy as np
from matplotlib import pyplot as plt
from NTCONST import world
import json

world_ids = [world_item[0] for world_item in world]
almost_nothing =(1-np.nextafter(1, 0))

def get_history_dict():
    """
    loads the history.json file and returns it as a dictionary
    """
    with open("output/history.json", "r") as jsonfile:
        return json.load(jsonfile)


history_dict = get_history_dict()


def get_average_kills(history_dict=history_dict):
    average_kills = np.mean([int(run["kills"]) for timestamp, run in history_dict.items()])  # calculate average kills from history dictionary
    return average_kills


def get_death_probabilities(history_dict=history_dict):
    # A monstrous one-liner that creates a dictionary
    death_probabilities = {f"{loops}-{world_id}-{level}":
                               (sum([bool((
                                   run["world"] == str(world_id) and run["level"] == str(level) and run["loops"] == str(loops))
                                   and not run["world"] in ["107","106","100"])
                                   for run in history_dict.values()])
                                    /
                                (almost_nothing + sum([bool(
                                 ((int(run["level"]) >= level and int(run["world"][-1]) == int(world_id[-1]) and int(run["loops"]) == loops) or
                                                                 (int(run["world"][-1]) >  int(world_id[-1]) and int(run["loops"]) == loops) or
                                                                                                        (int(run["loops"]) > loops)
                                   and not run["world"] in ["107","106","100"]) or (world_id in ["107","106","100"]))
                                   for run in history_dict.values()])))
                                   for world_id in world_ids
                                   for level in [0, 1, 2, 3] 
                                   for loops in range(10)}  # (times_you_died_in_this_level OR ANY LEVEL BEFORE IT / time_you_died_ever) for each level

    """only the runs that are still goin at this point are counted
       so only the current run as well as all the runs that went on for longer than the current run
       see logic statements above
       YV's mansion, IDPDHQ and Crownvaults are all excepted bc. they can be visited at different times their prob. is zero for now
    """
    return death_probabilities


def get_from_history(*args):
    """
    Input: 
        Keywords for the required values eg. average_kills, death_probabilities etc.
    Output:
        The calculated values for the requested input arguments in a dictionary
    """

    argument_dict = {"average_kills": get_average_kills, "death_probabilities": get_death_probabilities}

    for argument in args:  # this stops the code and throws an error but it could be changed to warnings instead
        assert (argument in argument_dict.keys()), "Requested argument cannot be fetched from api"

    if len(args) > 1:
        return {argument: argument_dict[argument]() for argument in args}  # calls the get_ function for each argument
    else:
        return argument_dict[args[0]]()

def plot_probabilities():


    
    
    death_probabilities = get_death_probabilities()
    kees = list(death_probabilities.keys())
    redundant_lvls = ["-0-2","-0-3","-2-2","-2-3","-4-2","-4-3","-6-2","-6-3","-10"]
    kees = [ key for key in kees if not any((redundant_lvl in key or key.endswith("-0")) for redundant_lvl in redundant_lvls)]# remove special levels
    kees.sort()
    limiter = list([death_probabilities[_] for _ in kees]).index(1.0)+1

    fig = plt.figure(figsize=(8, 4.5))

    ax = fig.add_subplot(111)

    sorted_values = [1-death_probabilities[_] for _ in kees]

    ax.plot(kees[:limiter],sorted_values[:limiter],'k')
    ax.xaxis.set_ticks(kees[:limiter][::3])
    ax.fill_between(kees[:limiter],[0 for _ in range(len(kees))][:limiter],sorted_values[:limiter],color='limegreen',alpha=0.2,label='LIFE')
    ax.fill_between(kees[:limiter],[1 for _ in range(len(kees))][:limiter],sorted_values[:limiter],color='r',alpha=0.2,label='DETH')
	
    ax.set_title(label = f"P of Death | {limiter} logged deaths")
    ax.set_xlabel("Level - [Loop-World-Level]")
    ax.set_ylabel("Probability Surviving to the next Level")

    plt.legend()
    plt.show()

if __name__ == "__main__":
    history_dict = get_history_dict()
    history_values = get_from_history("average_kills", "death_probabilities")
    average_kills, death_probabilities = history_values["average_kills"], history_values["death_probabilities"]

    plot_probabilities()


