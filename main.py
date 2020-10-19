''''
 This program is a chatbot
 ->  This bot will start with a greeting and asks for name of the person
 ->  Next, this will greet the person  and asks the person what he want to do where bot will offer a set of options. 
 ->  Next, based on the person's input it will perform that particular task and gives results.

'''
import random
from interactive_dictionary import getMeaning
from equations import solve_equations
def introduction():
     messages = ["Hi there! My name is Tom"]
     return random.choice(messages)

def welcome_greetings(name):
    messages = ["I can help you to do the below tasks"]
    s = "Hey "+name+"! "
    return  s+random.choice(messages)


def menu():
    print("1.Calculating an expression") 
    print("2.Dictionary")
    print("3.Solving an equation")
    print("4.Exit")
    print("############################")
    try:
        return int(input("Enter your choice [1-4]: "))
    except:
        print("Please, enter your choice in between 1-4")   


def calculate():
    xpression = input("Enter an expression: ")
    #if expression was valid then it will print the result
    try: 
        print("Result = ",str(eval(xpression)))
    #else we will throw error message
    except Exception as e:
        print(str(e))
def word_meaning():
    #take word from user
    word = input('Enter the word: ')

    #function call to get meaning of the word entered by user
    meaning = getMeaning(word)

    #printing meaning of the word in console
    if type(meaning) == list:
        for item in meaning:
            print(item)
    else:
        print(meaning)

def main():
    print(introduction())
    name = input("Please enter your name: ")
    print(welcome_greetings(name))
    choices  = menu()
    #repeat showing menu until user wants to exit
    while(choices != 4):
        if(choices == 1):
            calculate()
        elif(choices == 2):
            word_meaning()
        elif(choices ==3 ):
            solve_equations()
        else:
            print("Your choice is wrong. Please enter only the avaible choices")
        choices = menu()

main()
