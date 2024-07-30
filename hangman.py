#coding=utf-8
import random

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

# ======כאן יש להוסיף אוסף של מילים=====
secretWords = ['hello', 'love', 'pleas', 'tanks', 'peace', 'python', 'happy', 'sad', 'lovely', 'bool', 'map',
              'computer', 'python', 'good luck', 'family', 'welcome', 'grate']


# ============כאן יכתבו הפונקציות=============
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print(missedLetters)
    for i in range(len(secretWord)):
        ezer = False
        for x in range(len(correctLetters)):
            if secretWord[i] == correctLetters[x]:
                print(secretWord[i], end=" ")
                ezer = True
        if (ezer == False):
            print("_", end=" ")

def getGuess(alreadyGuessed):
    g = input("guess a letter: ")
    while g in alreadyGuessed or g.isalpha() == False or len(g) > 1:
        g = input("you have been wrong... input again: ")
    return g

def playAgain():
    answer = input("do you wont to play again? input yes or no")
    if (answer.startswith("yes")):
        return True
    return False


# ========כאן תחילת המשחק================

missedLetters = ''
correctLetters = ''
gameIsDone = False
secretWord = secretWords[random.randint(0, len(secretWords) - 1)]
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    print("")
# המשתמש מקיש אות ובודקים אם זה תקין
    guess = getGuess(correctLetters + missedLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        # בדיקה אם השחקן ניצח
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # בדיקה האם השחקן הפסיד
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(
                len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
    # האם השחקן רוצה לשחק שוב??
    # אתחול המשתנים והמשחק מתחדש...
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = secretWords[random.randint(0, len(secretWords) - 1)]
        else:
            break
