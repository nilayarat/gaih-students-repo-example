#HANGMAN GAME day 5 HOMEWORK

import random
words = ["leon", "apple", "summer", "banana", "book"]
guess_number = 5
characters = [] #this list created to add using letters in case of repeating 
x = len(word)
z = list('_' * x)
print(' '.join(z), end='\n')

while guess > 0:
    y = input("Guess a letter : ")
    if y in caharacters:
        print("Alreay used...")
        continue
elif len(y) > 1:
        print("Please enter one letter.")
        continue
elif y not in word:   #if giving letter not exist in word
        guess_number -= 1
        print("Wrong Guess!. You have {} guess.".format(guess_number))
else:
      for i in range(len(word)):
      if y == word[i]:
      print("True Guess")
      z[i] = y
      characters.append(y)
      print(' '.join(z), end='\n')
answer = input("Do you want to guess whole word? ['y' or 'n'] : ")

if answer == "e":
    guess = input("You can guess whole word : ")
    if guess == word:
    print("Congrats!")

        break
 else:
    guess_number -= 1
    print("Wrong Guess!. You have {} guess.".format(guess_number))


    if guess_number == 0:
    print("You have no guess.You Lost! The man Hang.")

    break
