#HANGMAN
importing time module
import.time
#wait for 1 second
time.sleep(1)

print "Guess!"
time.sleep(0.5)

#here we set the secret
word = "flover"

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 7

# Create a while loop
#check if the turns are more than zero
while turns > 0: 
# make a counter that starts with zero
    failed = 0             

# for every character in flover_word    
    for char in word:      

# see if the character is in the players guess
        if char in guesses:    
    
 # print then out the character
            print char,    

        else:
# if not found, print a dash
            print "_", 
	
# and increase the failed counter with one
            failed += 1    

# if failed is equal to zero

# print You Won
    if failed == 0:        
        print "You won"  
# exit the script
	break
       
