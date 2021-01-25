import numpy
import die #lol same bro
history_dict={}

def get_history_dict():
    """
    loads the history.json file and returns it as a dictionary
    """
    with open("output/history.json","r") as jsonfile:
        return json.load(jsonfile)


def get_average_kills(history_dict=history_dict):
    average_kills = False #TODO calculate from history dictionary
    return average_kills

def get_death_probabilities(history_dict=history_dict)
    death_probabilities = False #TODO see above
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