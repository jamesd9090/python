# Convert text file into string
with open('word_list.txt', 'r') as file:
    word_string = file.read().replace('\n', ' ')

# Split string into list
word_list = word_string.split()

import random

# Choose word at random from list using rdm number gen
word_select = random.randint(0,99)
chosen_word = word_list[word_select]

# Creat hangman board to print out for each life
life0 = ['               ']*9
life1 = ['|___________   ',' ',' ',' ',' ',' ','               ',' ', ' ']
life2 = ['|___________   ','|              ','|              ','|              ','|              ','|              ','|              ','|              ',' ']
life3 = ['|___________   ','|              ','|              ','|              ','|              ','|              ','|              ','|              ','_______________']
life4 = ['|___________   ','|              ','|              ','|              ','|              ','|              ','|          O   ','|          |   ','_______________']
life5 = ['|___________   ','|              ','|              ','|              ','|              ','|        --|-- ','|          O   ','|          |   ','_______________']
life6 = ['|___________   ','|              ','|           )  ','|           )  ','|          |   ','|        --|-- ','|          O   ','|          |   ','_______________']
life7 = ['|___________   ','|              ','|         ( )  ','|         ( )  ','|          |   ','|        --|-- ','|          O   ','|          |   ','_______________']

def hangman_board(life):
	if life == 0:
	    print(life0[8])
	    print(life0[7])
	    print(life0[6]+'     7 lives remaining')
	    print(life0[5])
	    print(life0[4])
	    print(life0[3])
	    print(life0[2])
	    print(life0[1])
	    print(life0[0])
	    
	elif life == 1:
	    print(life1[8])
	    print(life1[7])
	    print(life1[6]+'     6 lives remaining')
	    print(life1[5])
	    print(life1[4])
	    print(life1[3])
	    print(life1[2])
	    print(life1[1])
	    print(life1[0])
	    
	elif life == 2:
	    print(life2[8])
	    print(life2[7])
	    print(life2[6]+'     5 lives remaining')
	    print(life2[5])
	    print(life2[4])
	    print(life2[3])
	    print(life2[2])
	    print(life2[1])
	    print(life2[0])

	elif life == 3:
	    print(life3[8])
	    print(life3[7])
	    print(life3[6]+'     4 lives remaining')
	    print(life3[5])
	    print(life3[4])
	    print(life3[3])
	    print(life3[2])
	    print(life3[1])
	    print(life3[0])

	elif life == 4:
	    print(life4[8])
	    print(life4[7])
	    print(life4[6]+'     3 lives remaining')
	    print(life4[5])
	    print(life4[4])
	    print(life4[3])
	    print(life4[2])
	    print(life4[1])
	    print(life4[0])

	elif life == 5:
	    print(life5[8])
	    print(life5[7])
	    print(life5[6]+'     2 lives remaining')
	    print(life5[5])
	    print(life5[4])
	    print(life5[3])
	    print(life5[2])
	    print(life5[1])
	    print(life5[0])

	elif life == 6:
	    print(life6[8])
	    print(life6[7])
	    print(life6[6]+'     1 life remaining')
	    print(life6[5])
	    print(life6[4])
	    print(life6[3])
	    print(life6[2])
	    print(life6[1])
	    print(life6[0])

	else:
	    print(life7[8])
	    print(life7[7])
	    print(life7[6]+'     YOU LOSE!!!')
	    print(life7[5])
	    print(life7[4])
	    print(life7[3])
	    print(life7[2])
	    print(life7[1])
	    print(life7[0])

# Function prints out *'s and letters based on inputted guess
def hidden_word(word,letter):
    
    for char in word:
        if char in letter:
            print(char, end='')
        else:
            print("*", end='')

# Lose check, lose if user gets to 7 lives
def lose_check(lives):
    
    if lives == 7:
        return True
    else:
        return False

# Function to return unique letters in a given string
# Use to compare guessed letters vs chosen word
# Allows user to accidentally input a correct letter multiple times without affecting result
def unique_letters(word):
    unique_list = []
    
    for i in word:
        if i not in unique_list:
            unique_list.append(i)
        else:
            continue
    return unique_list

# Compare length of unique string of guessed letters vs length of unique string of chosen word
# If lengths are equal player has guessed all letters and therefore wins.
def win_check(word1,word2):
    
    if len(unique_letters(word1)) == len(unique_letters(word2)):
        return True
    else:
        return False


# SETUP
# Set life count = 0 
# Set playing = True 
# Set correct letters string = []
life = 0 
playing = True
correct_letters = []

# Welcome message and rules
print('\nWelcome to Hangman!')
print('\nYou have 7 attempts to guess the word.')
print('\nGuess letters a-z.')
hangman_board(life)
#Print out *'s to represent number of characters in chosen word
hidden_word(chosen_word, correct_letters)
print('')

# Start while loop for if playing or not
while playing:
	guess = ' ' 
	# Start while loop for for blank guess
	while guess == ' ':
		print('')
		guess = input('Please enter your next guess: ')
		# If guess not a valid letter of the alphabet, return to start
		if guess not in 'abcdefghijklmnopqrstuvwxyz':
		    hangman_board(life)
		    print('')
		    hidden_word(chosen_word, correct_letters)
		    print('\nCharacter not accepted, please enter a letter a-z')
		    guess = ' '
		# If guessed letter not in chosen word, increase life count and conduct lose check
		elif guess not in chosen_word:
		    life = life + 1
		    print("\nLetter Incorrect!!!")
		    hangman_board(life)
		    print('')
		    hidden_word(chosen_word, correct_letters)
		    print('')
		    if lose_check(life):
		    	print('')
		    	print(chosen_word)
		    	print('')
		    	print("YOU LOSE")
		    	playing = False
		    else:
		        guess = ' '

		else:
			# If guess correct, add guess to correct_letters list. Conduct win check.
		    correct_letters.append(guess)
		    print("\nLetter Correct!!!")
		    hangman_board(life)
		    print('')
		    hidden_word(chosen_word, correct_letters)
		    print('')
		    if win_check(chosen_word, correct_letters) == False:
		        guess = ' '
		    else:
		    	print('')
		    	print("CONGRATULATIONS YOU WIN")
		    	playing = False