# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in lettersGuessed:
        
        if char in secretWord:
            secretWord=secretWord.strip(char)
        if len(secretWord)==0:
            return True
        else:
            return False

    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result=['_']*len(secretWord)
    for char in lettersGuessed:
        if char in secretWord:
            for i in range(len(secretWord)):
                if secretWord[i]==char:
                    result=result[:i]+list(char)+result[(i+1):]
    return ' '.join(result)
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result=list(string.ascii_lowercase)
    for char in lettersGuessed:
        if str(char) in result:
            result.remove(char)
    return ''.join(l)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    print("-------------")
    lettersGuessed=[]
    guessRemain=8
    while True:
        print("You have {} guess left".format(guessRemain))
        print("Available letters: abcdefghijklmnopqrstuvwxyz")
        guess=input("Please guess a letter: ")
        g=getGuessedWord(secretWord, lettersGuessed)
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: "+g)
            print("-------------")
            continue
        elif guess not in lettersGuessed:
            lettersGuessed.append(guess)
        if guess in secretWord:
            print("Good guess: "+g)
            print("-------------")
            if isWordGuessed(secretWord, lettersGuessed):
                return "Congratulations, you won!"
            continue
        else:
            print("Oops! That letter is not in my word: "+g)
            print("-------------")
            if guessRemain==1:
                return "Sorry, you ran out of guesses. The word was"+secretWord
            else:
                guessRemain-=1
        
        
    



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
