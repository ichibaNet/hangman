import random
print("Welcome To The Hangman By Avihai, Try not to be HANG ;)")
print(" _    _")
print("| |  | |")
print("| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __")
print("|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
print("| |  | | (_| | | | | (_| | | | | | | (_| | | | |")
print("|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
print("                     __/ |")
print("                    |___/")

# set up some constants
HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|   /|
| 
|   
|   
|   
|   
--------
""",
"""
------
|    |
|    O
|   /|\ 
|   
|   
|   
|   
|   
--------
""",
"""
------
|    |
|    O
|   /|\ 
|   /
|   
|   
|   
|
--------
|    |
|    O
|   /|\ 
|   / \ 
|   
|   
|   
|
""")


MAX_WRONG = len(HANGMAN) - 6
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON".lower())

# initialize variables
word = random.choice(WORDS) # the word to be guessed
so_far = "-" * len(word)      # one dash for each letter in word to be guessed
wrong = 0                   # number of wrong guesses player has made
used = []              # letters already guessed



print("Welcome to Hangman.  Good luck!")
print()


# Blank the secret word
secret_word = []

# Blank the letters guessed
old_letters_guessed = []


letter_guessed = input("Guess a letter: ")
if len(letter_guessed) != 1 or not letter_guessed.isalpha():
    print('Error: Please enter a single letter!')
else:
    print(letter_guessed.lower())


if letter_guessed in [word]:
    print("\nYes!", letter_guessed, "is in the word!")
    # create a new so_far to in
    # include guess
    new = ""
    for i in range(len(word)):
        if letter_guessed == word[i]:
            new += letter_guessed
        else:
            new += so_far[i]
    so_far = new
else:
    print("\nSorry,", letter_guessed, "isn't in the word.")
    wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")



# print the old_letters_guessed
print('X\n',' -> '.join(sorted(old_letters_guessed)))

# Function to check if the input from the player is valid
def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    return True


# Function to update the letter guessed by the player
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
  if letter_guessed.isalpha() and len(letter_guessed) == 1 and letter_guessed.lower() not in old_letters_guessed:
    old_letters_guessed.append(letter_guessed)
    return True
  else:
    print('X\n',' -> '.join(sorted(old_letters_guessed)))
    return False



# Function to show the hidden word
def show_hidden_word(secret_word, old_letters_guessed):
    result = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            result += letter + " "
        else:
            result += "_ "
    print(show_hidden_word(secret_word, old_letters_guessed))

# Function to check whether the player has won the game
def check_win(secret_word, old_letters_guessed):
  for char in secret_word:
    if char not in old_letters_guessed:
      return False
  return True

# Check if wrong or right
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    letter_guessed = input("\n\nEnter your guess: ")
    guess = letter_guessed.lower()
    continue

while letter_guessed in used:
        print("You've already guessed the letter", letter_guessed)
letter_guessed = input("Enter your guess: ")
letter_guessed = letter_guessed.lower()
if check_win(word, old_letters_guessed):
    print("\nYou guessed it!")
print("\nThe word was", word)



