
import random

logo = '''
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               
'''
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    
words = ['toronto','taiwan','brunei','austria','uruguay','romania','vietnam','mongolia','angola','serbia','kuwait']
print(logo)
guessWord = random.choice(words)

checkList = []
for i in guessWord:
    checkList.append('_')

for i in checkList:
    print(i,end=' ')
print()

condition = True
live = 0
while condition:
    letter = str(input('Guess Letter: ')).lower()
    flag = False
    for i in range(len(guessWord)):
        if letter == guessWord[i]:
            checkList[i] = letter

    for i in checkList:
        print(i,end=' ')
    print()

    if letter not in guessWord:
        print(HANGMANPICS[live])
        live += 1
        

    if not '_' in checkList:
        condition = False
        Result = 'Win'
    if live == 7:
        condition = False
        Result = 'Lose'

else:
    print(f'You {Result}!')