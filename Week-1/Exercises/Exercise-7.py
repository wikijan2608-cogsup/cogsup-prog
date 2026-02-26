"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

# computer guessing game 
from random import randint

# opening messages
print("Think of a number between 1 and 100, and I will try to guess it!")
print("After each guess, type:")
print("  'correct' if I guessed your number")
print("  'higher' if your number is higher than my guess")
print("  'lower' if your number is lower than my guess")

# range of possible numbers determined
lowest = 1
highest = 101 # to enable guessing 100

correct = False # did the computer guess correctly? 

while not correct:
    trial = randint(lowest, highest-1) # computer makes a guess
    # ask human for feedback
    feedback = input(f"My guess is {trial}. Is it correct?").strip().lower()
    # human needs to type either "correct", "higher" or "lower" to help the computer guess
    while feedback not in ["correct", "higher", "lower"]:
        print("Please, type correct, higher or lower")
        feedback = input(f"My guess is {trial}. Is it correct?").strip().lower()
    
    if feedback == "correct": #if guessed correctly 
        correct = True   

    elif feedback == "higher": # if feedback is higher, than new lower bound is the current guess
        lowest = trial
    
    elif feedback == "lower": # if feedback is lowwer, than new higher bound is the current guess
        highest = trial





        






