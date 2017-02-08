import random


apple = random.randint(0,3)
banana = random.randint(0,6)
berry = random.randint(0,10)


count = []
Total_Cards_in_play = []
value = []

def deck3():
    return apple #returns a random number between 0 and 3

def deck6():
    return banana #returns a random number between 0 and 6

def deck10():
    return berry #returns a random number between 0 and 10


def main():
    operation = input("Choose a selection of deck sizes 3 , 6 , 10 : ") #asks deck size selection
    if(operation != '3' and operation != '6' and operation != '10'): # selects your deck size
        print("Ener a valid operation") # if the input is not 3,6,10 the program ends and asks for valid operation


def computer(): # defines functions
    opera = input("Would you like to  play against the computer? [y/n] : ") # input asks if player would like to play against the computer
    if(opera != 'y' and opera != 'n'): # carries on the function
        print("That is not valid") # if answer is 'n' function ends
    else:
        if(opera == 'y'): ##### FINISH
            pass
        
 # ends function

def person1(): # defines function
    return
if(computer > person): # if computer is larger than person
    print("computer is the winner!") # prints computer is winner
    return count.append(1) + Total_Cards_in_play.append(1) # appends total count and cards in play
    else:
        if(person > computer): # if person is larger than computer
            print("You are the winner!") # prints person is larger than computer
            return count.append(1) + Total_Cards_in_play.append(1) # appends total count and cards in play
        else:
            if(person == computer): # if it is a draw 
                print("It is a draw") # prints draw
                ask = input("Would you like to play again? [y/n] : ") # asks if u want to play again
                if(ask == 'y'):
                    return main  # attempts to restart program

                        
    


person1()


# To do
# set computer and person to random variable integars
# create a re run if draw
# create against computer or person
# finish computer()

        
