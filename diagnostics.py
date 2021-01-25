import numpy
import die #lol same bro
from NTCONST import world
world_ids = [world_item[0] for world_item in world]
history_dict={}

def get_history_dict():
    """
    loads the history.json file and returns it as a dictionary
    """
    with open("output/history.json","r") as jsonfile:
        return json.load(jsonfile)


def get_average_kills(history_dict=history_dict):
    average_kills = avg([run["kills"]for timestamp,run in history_dict.items()]) #calculate average kills from history dictionary
    return average_kills

def get_death_probabilities(history_dict=history_dict)
    death_probabilities = {f"{world}-{level}" :
                            (sum([run["world"]==world and run["level"] ==level for run in history_dict.values()])/len(history_dict.values()))
                            for world in world_ids for level in [1,2,3]}#(times_you_died_in_this_level / time_you_died_ever) for each level
    """
    TODO
    -what level is the api displaying in secret worlds?
    -do the levels start at 0 or at 1?
    """
    return death_probabilities
    
def get_from_history(*args)
    """
    Input: 
        Keywords for the required values eg. average_kills, death_probabilities etc.
    Output:
        The calculated values for the requested input arguments
    """
    
    argument_dict={"average_kills":get_average_kills, "death_probabilities":get_death_probabilities}
    
    for argument in args: #this stops the code and throws an error but it could be changed to warnings instead
        assert (argument in argument_dict.keys()), "Requested argument cannot be fetched from api"
    
    return [argument_dict[argument]() for argument in args] #calls the get_ function for each argument




if __name__ == "__main__":
    history_dict = get_history()
    average_kills,death_probabilities = get_from_history("average_kills","death_probabilities")