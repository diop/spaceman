import random

print('----------------------------------------------')
print('              SPACEMAN WORD GAME')
print('----------------------------------------------')

def load_words():
    f = open('spaceman_words.txt', mode = 'r')
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
    matches = 0
    match = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
            matches += 1
            match += letter
        else:
            guessedWord += '_'

    if matches > 1:
        print(f'Congrats! The word contains {matches} matches')
    elif matches == 1:
        print(f'Congrats! The word contains the letter {match}.')
    else:
        print(f'Error! The word does not contain the letter you entered.')

    return guessedWord

def get_available_letters(lettersGuessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters_choices = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print(letters_choices)
    for letter in lettersGuessed:
        if letter in letters_choices:
            letters_choices.remove(letter)
    return letters_choices

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
    word_length = len(secretWord)
    letters_guessed = []
    print('Please enter your name: ')
    name = input(':> ')
    print(f'Hi {name}! Welcome to Spaceman Word Game. The word to guess contains {word_length} letters. Good luck!')
    while not is_word_guessed(secret_word, letters_guessed):
        print('Guess a letter in the word.')
        guess = input(':> ').upper()
        if guess not in letters_guessed:
            letters_guessed.append(guess)
            available_letters = get_available_letters(letters_guessed)
            print(f'Letters you have not yet used: {available_letters}')
            print(f'Your word status: {get_guessed_word(secret_word, letters_guessed)}')
        else:
            print(f'You have already used that letter. Pick another one!')
    else:
        print(f'You guessed the word: {secret_word}!!! ')
secret_word = load_words()
spaceman(load_words())
