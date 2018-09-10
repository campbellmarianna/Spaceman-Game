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
   #print("secret_word: " + secret_word)
   return secret_word
load_word()

 # Count the number of characters in a string
def countLetters(letter):
     len(letter)

 #     secret
#countLetters(str(pie))
