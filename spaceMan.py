import random

def load_word():
    # Open - a built in function , open file and return a file object; 'r' - open for reading default
    # Open a file
   f = open('words.txt', 'r')
   # Test function: print("Read Line: %s" % (f))
   #.readlines - a method, read and return the list of all logical lines remaining in the current file
   words_list = f.readlines()
   # Close open file
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word
   # Testing input from words.txt
   # return len(secret_word)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in secret_word:
        if l not in letters_guessed:
            return False
    return True
#----Trying to understand what I am doing. --------------------------------------------------------------
    # secret_word = random.choice(words_list) not needed, called in a function on line 15
    # test_word = "lalala"
    # test_secret_word = "blahblahblah"
    # len(secret_word)
    # Add some logic to test if the guessed word == the secret word
    # if test_word is test_word:
    #     return True
    # return False
    # return the result of that logic as either true or false

# # is_word_guessed(secret_word, letters_guess)
# secret_word = load_word()
# print(is_word_guessed(secret_word, letters_guessed)) # returns a boolean
#---------------------------------------------------------------------------------------------------------

def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # declare a variable with a empty string to append
    word = ""
    #loop through secret_word and get individual letters
    for letter in secret_word:
        #if the letter from the secret_word is in letters guessed
        if letter in letters_guessed:
            # if true append it in the word variable
            word += letter + ""
        # else append the word variable with a underscores
        else:
            word += "_ "
        # return the word variable
    return word


def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #create a variable with choices left which is the alphabet
    choices = list("abcdepghijklmnopqrstuvwxyz")
    #Create a loop
    for letter in letters_guessed:
        #If the letters in letter_guessed are the letters in choices you remove it
        if letter in choices:
            choices.remove(letter)
    #return what is left
    return choices

# Loop template for reference
# running = True
# while running():
#     getLetter = user_input(
#         "Hi This is Spaceman! You have to guess a letter of a word? -
#         What will your letter be: ")
#     running = select(getLetter)


# Testing code:
# def test():
#     user_value = input("Hi! This is Spaceman! Guess letter in the secret word.
#     You have __ chances to guess letters in the secret word.")
#     print(user_value)
#
# test()

def user_input(prompt):
        # the input function will display a message in the terminal
        # and wait for user input.
        user_input = input(prompt)
        return user_input


def is_given_guess_correct(guessed_letter, secret_word):
    print("Secret word {}".format(secret_word))
    if guessed_letter in secret_word:
        return True
    else:
        return False


# count = 0
def life(count):
    if count == 7:
        print("  O ")
    if count == 6:
        print("  O ")
        print("  | ")
    if count == 5:
        print("  O ")
        print("  | ")
        print(" / ")
    if count == 4:
        print("  O ")
        print("  | ")
        print(" / \ ")
    if count == 3:
        print("  O ")
        print(" -| ")
        print(" / \ ")
    if count == 2:
        print("|   O   |")
        print("|  -|-  |")
        print("|  / \  |")
    if count == 1:
        print("   / \      ")
        print("  /   \     ")
        print(" /     \    ")
        print("|   O   |   ")
        print("|  -|-  |   ")
        print("|  / \  |   ")
        print(" \_____/    ")
    if count == 0:
        print("||        ||")
        print(" BLAST OFF!!")
        print("   / \      ")
        print("  /   \     ")
        print(" /     \    ")
        print("|   O   |   ")
        print("|  -|-  |   ")
        print("|  / \  |   ")
        print(" \_____/    ")
        print(" |||||||   ")
        print("No more guesses! You lose.")

def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Spaceman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    secret_word_len = len(secret_word)
    letters_guessed = []
    count = 8
    # Hi This is Spaceman! You have to guess letters in the secret word.
    # The secret word contains len(secret_word) letters.
    # You can guess one letter per round. What will your letter be?
    print("Hi This is Spaceman! You have to guess letters in the secret word.")
    print("The secret word contains {} letters.".format(secret_word_len))
    print("There are only 7 rounds. You can guess one letter per round.")
    # Store value from user in letter_guessed, an empty list - no need add
    #the letter to the letters_guessed list
    # Check if guessed letter is a single characher if else statement
    # if len(guessed_letter) == 1:
    #      letters_guessed.append(guessed_letter)
    # else:
    #     print("Please return a single letter")
    # while the letter is not guessed right continue to play the game
#while count < 7:
    while is_word_guessed(secret_word, letters_guessed) == False and count > 0:
        guessed_letter = input("What will your letter be? ")
        # if the user's input is not in the letter's already guessed lists
        if guessed_letter not in letters_guessed:
            # append the new letter into the lists
            letters_guessed.append(guessed_letter)
            print("The letters you have not yet guessed are: {}".format(get_available_letters(letters_guessed)))
            # show the word with underscores and the correct letters in order
            print("You are still missing these letters: {}".format(get_guessed_word(secret_word, letters_guessed)))

            #

            # if is_word_guessed(secret_word, letter_guessed) is not True:
            # if is_word_guessed(secret_word, letters_guessed):
            #     print("The letters you have not yet guessed are: {}".format(get_available_letters(letters_guessed)))
            #     # show the word with underscores and the correct letters in order
            #     print("You are still missing these letters: {}".format(get_guessed_word(secret_word, letters_guessed)))

            if is_given_guess_correct(guessed_letter, secret_word):
                print("CORRECT!!")
                life(count)
                print(count)
            else:
                print("NOt correct")

                # Take away a life if guessed_letter equal length of secret words #life = life - 1
                count -= 1
                life(count)
                print(count)

        else:
            # if the letter is in the letters guessed list print the following
            print("Guess another letter that you have not chosen yet.")
            print("The letters you have not yet guessed are: {}".format(get_available_letters(letters_guessed)))
            print("You are still missing these letters: {}".format(get_guessed_word(secret_word, letters_guessed)))
    else:
        # once the loop returns False print the message that the user won
        if count == 0:
            print("You lost. The word was {}".format(secret_word))
        else:
            print("Good Job! You won!")


# else:
#     print("You have no more chances to guess. You have loss the game.")


spaceman(load_word())
