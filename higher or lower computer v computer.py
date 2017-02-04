import random
print("""This is higher or lower game,
The computer vs the computer!
""")

apple = random.randint(0,100)
banana = random.randint(0,100)
can = apple > banana
can2 = banana > apple

def side():
    if can == True :
        print("Computer one has won!")

        if can2 == True :
            print("The other computer has won!")

            if banana == apple :
                print("Unfortunately it is a draw :(")


side()

  
def main():
    if can == True :
        print("Computer one has won!")

        if can2 == True :
            print("The other computer has won!")

            if banana == apple :
                print("Unfortunately it is a draw :(")
    while True:
        again = input("Would you like to play again? Enter y/n: ")

        if again == "n":
            print ("Thanks for Playing!")
            return
        elif again == "y":
            print ("Lets play again..")
            for _ in range(3):
                side()
            
        else:
            print ("You should enter either \"y\" or \"n\".")

if __name__ == "__main__":
    main()


 
