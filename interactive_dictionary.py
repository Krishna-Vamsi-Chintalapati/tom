"""
 In this we will search for the meaning of the word in which it checks for the word in dictionary if not available will
  try to show closely matched word and then will if he wants

"""


import json
from difflib import get_close_matches

#load JSON data
data = json.load(open("data.json"))

#function to get the meaning of the word
def getMeaning(w):
    #Intially convert the word to lower to avoid case sensitivity
    w = w.lower()
    #if word exists then return corresponding meaning
    if w in data:
        return data[w]
    #else give meaning of the closely matched word if the word he was searching was same 
    elif len(get_close_matches(w,data.keys())) > 0:
        close_match = get_close_matches(w,data.keys())[0]
        print("Did you mean %s instead? Enter Y if yes or N if no: " % close_match)
        choice = input()
        choice = choice.lower()
        if choice == 'y':
            return data[close_match]
        elif choice == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "Sorry, We didn't understand your entry."
    else:
        return "The word doesn't exist in our dictionary."


