#### additional stuff to work on
# dont accept kanji if its the last character
# convert katakana to hiragana
# add a japanese dictionary to verify nouns
# ignore smaller characters

# read in katakana
# import json

# with open('katakana.txt') as text:
#     letters = text.read()
    
# katakana = json.loads(letters)

# create a list to store used words
used = []

# changes when the player wants to quit
playing = 'y'

# stores the previously entered word
prev = None

print("Let's play!\n")

# continue unless the player wants to quit
while playing == 'y':
    # handle the case of the first round
    if len(used) == 0:
        word = input('(Enter "終わった" if you would like to quit)\nEnter a noun: ')
        # check if the user wants to quit
        if word == '終わった' or word == 'おわった':
            playing = 'q'
            break
        elif word[-1] == 'ん':
            print('You have entered an invalid word. Please try again.\n')
        else:
            prev = word[-1]
            used.append(word)
        
    else:
        word = input('Enter a noun that starts with '+ prev + ': ')
        # check if the user wants to quit
        if word == '終わった' or word == 'おわった':
            playing = 'q'
            break
        # then check the validity of the word
        elif word[-1] == 'ん' or word[0] != prev:
            print('You have entered an invalid word. Please try again.\n')
        # if the word is valid
        else:
            # add the word to the used list
            used.append(word)
            # update prev for the next round
            prev = word[-1]