# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in your code
random_range = 100
number = 0
count = 7


# helper function to start and restart the game
def new_game():
    global number, count, random_range
    number = random.randrange(0,random_range)
    print 
    print "New game begins!"
    if(random_range == 100):
        count = 7
        print "Input range 0 to 100"
    elif (random_range == 1000):
        count = 10
        print "Input range 0 to 1000"
    print "You have", count, "guesses left!"
 
    
    

# define event handlers for control panel
def range100():
    global random_range, count
    count = 7
    random_range = 100
    print
    # print "Input range 0 to 100"
    new_game()
    
    

def range1000():
    global random_range, count
    count = 10
    random_range = 1000
    print
   #  print "Input range 0 to 1000"
    new_game()
    
    
    
def input_guess(guess):
    guess = int(guess)
    global count
    if ((count >= 1) and (guess == number)):
        print
        print "Your guess was", guess
        print "You win!"
        print "The secret number was", number
        new_game()
            
    elif ((count >1) and (guess < number)): 
        print
        print "Your guess was", guess
        count = count - 1
        print "Higher!"
        print "You have", count, "guesses left!"
        
            
    elif ((count >1) and (guess > number)):
        print
        print "Your guess was", guess
        count = count - 1
        print "Lower!"
        print "You have", count, "guesses left!"
        
            
    elif (count == 1):
        count = count - 1
        print
        print "Game Over!"
        print "You have", count, "guesses left!"
        print "Your guess was", guess
        print "The secret number was", number
        new_game()
       

    
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)


# register event handlers for control elements
button1 = frame.add_button("Range is 0 to 100", range100, 200)
button2 = frame.add_button("Range is 0 to 1000", range1000, 200)
inp = frame.add_input("Your guess", input_guess, 200)


# call new_game and start frame
frame.start()
new_game()

# always remember to check your completed program against the grading rubric
