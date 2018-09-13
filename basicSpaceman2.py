# Taking another approach with Spaceman
# Create variable that contains the secret word
import random

# Create a list of words for the user to guess named answerlist, strings, separated by commas
answerlist = ["cool", "blessed", "learning", "growing", "pains"]
#random shelf answerlist
random.shuffle(answerlist)
# Set a variable called answer answerlist[0] - list(), it will chop it up and give me individual letters for my list take position 0 in the list - splet into indi letter
answer = list(answerlist[0])
# create an empty list called display
display = []
#create an empty list called used - same vaules that are display are in
used = []
# Use command extent to add different things in the variable into list called display
display.extend(answer)
# Test by printing display - Good idea to print to test things out
print(display)
# create a variable called incorrect set 5
incorrect = 0
"""loop - however long our word is ex:4 for each one replace that letter at that index with an underscores - use join to join the space inbetween the underscores so there is no spaces between the underscores - detail: add extra bit here if you would put in h loads of times you would win the game but have put in another condiitional here, we said if the answer is in guessed and it is in used we copied anything in display into used list then it remove that letter from our used list, so now that letter disappears
    #if I go through this conditional here and then it would go well h is in the answer
    # add if incorrect is greater than zero

    #add if guess is not display it will tell me Sorry wrong guess
        #add the thing that takes the value away from the counter, subtract one from incorrect guess"""
for i in range(len(display)):
    display[i] = "_"

# Test loop
print(display)
# Create a variable called count which will stop the game one the letters have been guessed - while count is less than the length of the answer and it will repeat all until we get to the length of This
    # We have a guess which is our input, of what we think the letter is going to be
    #I have converted everyhting to lowercase - because you see here everything up there is lowercase and anything they type in even if it is uppercase will become lowercase
    #I have printed count so I can see if it is
#Another loop responsibile for replacing the letters in the guessed word instead of underscore with the letter guessed then it adds one to the counter when it gets up to 4 it will end the game
# Print's out the new word with anything we have guessed already in it

# Print("You won!") - Make an if statement that if the count equals the length of the answer then print You win else print you have no more chances
