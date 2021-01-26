import numpy
from NTCONST import world
import json
world_ids = [world_item[0] for world_item in world]


def get_history_dict():
    """
    loads the history.json file and returns it as a dictionary
    """
    with open("output/history.json","r") as jsonfile:
        return json.load(jsonfile)
history_dict=get_history_dict()

def get_average_kills(history_dict=history_dict):
    average_kills = avg([run["kills"]for timestamp,run in history_dict.items()]) #calculate average kills from history dictionary
    return average_kills

def get_death_probabilities(history_dict=history_dict):
    #A monstrous one-liner that creates a dictionary
    death_probabilities = {f"{world_id}-{level}-{loops}" :
                            (sum([bool(run["world"]==world_id and run["level"]==str(level) and run["loops"]==str(loops)) for run in history_dict.values()])/len(history_dict.values()))
                            for world_id in world_ids for level in [0,1,2,3] for loops in range(20)}#(times_you_died_in_this_level / time_you_died_ever) for each level
    """
    TODO
    -what level is the api displaying in secret worlds?
    -do the levels start at 0 or at 1?
    """
    return death_probabilities
    
def get_from_history(*args):
    """
    Input: 
        Keywords for the required values eg. average_kills, death_probabilities etc.
    Output:
        The calculated values for the requested input arguments in a dictionary
    """
    
    argument_dict={"average_kills":get_average_kills, "death_probabilities":get_death_probabilities}
    
    for argument in args: #this stops the code and throws an error but it could be changed to warnings instead
        assert (argument in argument_dict.keys()), "Requested argument cannot be fetched from api"
	
    if len(args)>1:
        return {argument:argument_dict[argument]() for argument in args} #calls the get_ function for each argument
    else:
        return argument_dict[args[0]]()



if __name__ == "__main__":
    history_dict = get_history_dict()
    history_values = get_from_history("average_kills","death_probabilities")
    average_kills,death_probabilities = history_values["average_kills"],history_values["death_probabilities"]