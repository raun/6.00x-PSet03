import random
import string

WORDLIST_FILENAME = "words.txt"

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for e in secretWord:
        if e not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    res=''
    for e in secretWord:
        if e in lettersGuessed:
            res=res+e
        else:
            res=res+'_'
    return res



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    res=''
    for e in string.ascii_lowercase:
        if e not in lettersGuessed:
            res=res+e
    return res

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", str(len(secretWord)), "letters long."
    print "-------------"
    guessLeft=8
    lettersGuessed=[]
    while guessLeft>0 and not isWordGuessed(secretWord, lettersGuessed):
    	print "You have",str(guessLeft),"guesses left."
    	print "Available letters:",getAvailableLetters(lettersGuessed)
    	guess=str(raw_input("Please guess a letter: "))
    	guess=guess.lower()
    	while len(guess)!=1 and guess not in string.ascii_lowercase:
    		guess=str(raw_input("Please guess a new letter: "))
    	if guess not in lettersGuessed:
    		lettersGuessed.append(guess)
    		if guess in secretWord:
    			print "Good guess:",
    		else:
    			guessLeft-=1
    			print "Oops! That letter is not in my word",
    	else:
    		print "Oops! You've already guessed that letter:",
    	print getGuessedWord(secretWord, lettersGuessed)
    	print "------------"
    if isWordGuessed(secretWord, lettersGuessed):
    	print "Congratulations, you won!"
    else:
    	print "Sorry, you ran out of guesses. The word was", str(secretWord)

