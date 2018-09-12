'''
Read word from other file, is now the secret word

Display empty spaces for each letter of word and a blank list of letters guesssed

Prompt user for letter, check to make sure only lower case letters are inputted
First check length is only 1 character then try to find it in ascii_lowercase
If input is valid check secret word if it has those letters
Remove the letter from a list of all ascii_lowercase

Do above until all letters in word are guessed or 7 incorrect guesses are made

List of guessed letters can be made from ascii_lowercase then removing each guessed letter
'''


import random
import string
letters_left=string.ascii_lowercase + " "
rocket = [" ^ ", "| |","|o|","| |","|o|","/ \\","VVV"]

#Gets word and category from read files
def load_word():

    words = list()
    f = open('index.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    category = random.choice(words_list).strip()
    #print(category)
    words.append(category)

    f = open(category+'.txt','r')
    #f = open('testwords.txt','r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split('*')
    #for word in words_list:
    #    print(word)
    #    determine_difficulty(word,secret_word_no_duplicates(word))
    secret_word = random.choice(words_list).strip()
    #print(secret_word)
    words.append(secret_word)
    return words

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secret_word:
        #print(letter)
        index = letters_guessed.find(letter)
        if(index < 0):
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    #print(secret_word)
    #print(letters_guessed)
    displayed_word = ""
    for letter in secret_word:
        #print(letter)
        index = letters_guessed.find(letter)
        #print(index)
        if(index < 0):
            displayed_word = displayed_word + "_"
            #print(displayed_word)
        else:
            displayed_word = displayed_word + letter

    return displayed_word



def get_available_letters(letter_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    split_letters_left = letters_left.split(letter_guessed)
    return split_letters_left[0]+split_letters_left[1]

#Copyright Connor Oswold, RocketDrawer©
def draw_rocket(guesses_left):
    for index in range(0,7):
        if(7-guesses_left>index):
            print("|"+rocket[index])
        else:
            print("|")

def validate_input(guess, letters_guessed):

    if(len(guess) == 1):
        if(string.ascii_lowercase.find(guess) < 0):
            print("Error, guess is not a lowercase letter.")
            return False

        else:

            if(letters_guessed.find(guess) >= 0):
                print(guess + " has already been guessed")
                return False

    else:
        print("Error, input only one character.")
        return False

    #print("valid guess")
    return True

#Returns a string of the secret word with no duplicates. This allows for words with duplicate letters to be faster to check for complettion
def secret_word_no_duplicates(secret_word):

    no_duplicates_secret_word = ""
    for letter in string.ascii_lowercase:

        if(secret_word.find(letter) >= 0):

            if(no_duplicates_secret_word.find(letter) < 0):

                no_duplicates_secret_word = no_duplicates_secret_word + letter

    #print(no_duplicates_secret_word)
    return no_duplicates_secret_word

#Estimates difficulty of word based on:
#Is first letter of word a common letter (a, e, i, o, n, s, r, t)
#Number of letters that are an uncommon letter (j, q, x, z)
#Number of vowels / common letters
#Length of word (very short words are easy due to small number of them)
#Statistics taken from Oxford Dictionary
#Example of low difficulty word: Earth. Contains mostly common letters and no extremely rare letters while also short
#Example of high difficulty word: Quirky. Contains rare letters and less common letters and medium length
def determine_difficulty(secret_word,no_duplicates_secret_word):
    '''
    Attempt 1: I did not like this route because it did not seem very reflective of difficulty after testing. Should focus only vowels and number of unique letters.
    difficulty = 0
    num_unique_letters = len(no_duplicates_secret_word)
    num_vcommon_vowels = 0
    num_common_vowels = 0
    num_other_vowels = 0
    num_common_letters = 0
    num_rare_letters = 0
    num_uncommon_letters = 0
    is_first_letter_common_modifier = 1
    length_modifier = 0.2
    uniques_modifier = 2

    very_common_vowels = "ae"
    common_vowels = "io"
    other_vowels_and_common_letters = "urtnslc"
    uncommon_letters="dpmhgbfywkv"
    rare_letters = "jqxz"
    common_letters = "aeionsrt"

    if(len(secret_word)>12):
        length_modifier = 0.6
    elif(len(secret_word)>10):
        length_modifier = 0.8
    elif(len(secret_word)>8):
        length_modifier = 1
    elif(len(secret_word)>6):
            length_modifier = 0.8
    elif(len(secret_word)>4):
        length_modifier = 0.6

    if(num_unique_letters>12):
        uniques_modifier = 0.2
    elif(num_unique_letters>10):
        uniques_modifier = 0.4
    elif(num_unique_letters>8):
        uniques_modifier = .6
    elif(num_unique_letters>6):
        uniques_modifier = 0.8
    elif(num_unique_letters>4):
        uniques_modifier = 1

    if(common_letters.find(secret_word[0])>=0):
        is_first_letter_common_modifier = 0.8
    elif(uncommon_letters.find(secret_word[0])>=0):
        is_first_letter_common_modifier = 0.9
    elif(rare_letters.find(secret_word[0])>=0):
        is_first_letter_common_modifier = 1.1

    for letter in no_duplicates_secret_word:

        if(very_common_vowels.find(letter)>=0):
            num_vcommon_vowels += 1
        elif(common_vowels.find(letter)>=0):
            num_common_vowels += 1
        elif(other_vowels_and_common_letters.find(letter)>=0):
            num_other_vowels += 1
        elif(uncommon_letters.find(letter)>=0):
            num_uncommon_letters += 1
        elif(rare_letters.find(letter)>=0):
            num_rare_letters += 1

    difficulty += num_vcommon_vowels*0.2 * (10 / num_unique_letters)
    print("very common vowels: " + str(difficulty))
    difficulty += num_common_vowels*0.4 * (10 / num_unique_letters)
    print("common vowels: "+str(difficulty))
    difficulty += num_other_vowels*0.8 * (10 / num_unique_letters)
    print("other vowels: "+str(difficulty))
    difficulty += num_uncommon_letters*1.6 * (10 / num_unique_letters)
    print("uncommon letters: "+str(difficulty))
    difficulty += num_rare_letters*2* (10 / num_unique_letters)
    print("rare letters: "+str(difficulty))
    difficulty = difficulty * length_modifier * is_first_letter_common_modifier * uniques_modifier
    '''

    difficulty = 0
    num_unique_letters = len(no_duplicates_secret_word)
    vowels="aeiou"
    num_vowels = 0

    for letter in secret_word:

        if(vowels.find(letter)>=0):

            num_vowels += 1

    difficulty=int(10-10*(num_vowels/num_unique_letters))
    if(len(secret_word)<5):
        difficulty *= 0.2
    return difficulty

def spaceman(secret_word, category):
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
    # FILL IN YOUR CODE HERE...
    guesses_left = 7
    #Clears spaces in multi word secret words
    letters_guessed=" "
    letters_left=get_available_letters(" ")
    no_duplicates_secret_word = secret_word_no_duplicates(secret_word)
    difficulty = determine_difficulty(secret_word,no_duplicates_secret_word)

    #Clears screen to start game
    print("\033c")
    print("Welcome to Spaceman!")
    try:
        guess = input("Press RETURN to continue")
    except EOFError:
        print("\nWhat are you trying to pull punk?")
    while(guesses_left>0):

        #Prints guesses left, letters guessed and the secret word with already guessed letters and blanks
        print("Your word has " + str(len(secret_word)) + " letters in it. Category is " + category +".")
        print("You have " + str(guesses_left) + " incorrect guess(es) left.\nThese letters have been guessed so far: ")
        print(letters_guessed)
        print("Estimated (very rough estimate) of difficulty: " + str(int(difficulty)) + "/10")
        print("Secret word:")
        print(get_guessed_word(secret_word,letters_guessed))

        guess=""
        is_not_valid=True
        while(is_not_valid):
            try:
                guess = input("Please enter your guess (lowercase letter): ")
            except EOFError:
                print("\nPlease do not try to crash the program.")
            finally:
                is_not_valid=False

        #Condtionals to check input and give feedback to user based on guess
        if(validate_input(guess, letters_guessed)):

            letters_guessed = letters_guessed + guess
            letters_left=get_available_letters(guess)

            if(secret_word.find(guess) >= 0):

                print("You have correctly guessed a letter.")

                if(is_word_guessed(no_duplicates_secret_word,letters_guessed)):
                    print("Congradulations! You have guessed all the letters in " + secret_word + " with " + str(guesses_left) + " incorrect guess(es) left.")
                    raise SystemExit

            else:
                print(guess + " is not a letter in the secret word.")
                guesses_left -= 1


        draw_rocket(guesses_left)

    print("\033c")
    draw_rocket(guesses_left)
    print("You have run out of guesses.\n" + secret_word + " was the secret word. Please restart program if you would like to try again.")

#secret_word_no_duplicates("banana")
secret_word_category = load_word()
spaceman(secret_word_category[1],secret_word_category[0])
#spaceman("some spaces","test'")

#determine_difficulty("earth","areth")
'''print("testing")
print(letters_left)
letters_left=get_available_letters("a")
print(letters_left)
letters_left=get_available_letters("b")
print(letters_left)
print(is_word_guessed("banana",""))
print(get_guessed_word("banana",""))'''
