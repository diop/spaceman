import random

def load_words():
    f = open('words.txt', r)
    word_list = f.readlines()
    f.close()

    word_list = word_list[0].split(' ')
    secret_word = random.choice(word_list).upper()
    return secret_word

def is_word_guessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def get_guessed_word(secretWord, lettersGuessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    guessedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += '_'
    return guessedWord

def get_available_letters(lettersGuessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    for letter in lettersGuessed:
        #

def spaceman(secretWord):
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

# secret_word = load_word()
# spaceman(load_word())
