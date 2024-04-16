import random

# generating random numbers 
num= random.randint(1,30)

i=0

# giving users a range of chances to guess
# checking all possiblities to match the guess

for i in range(5):
    guess=int(input("enter the guess you made: "))

    if(num==guess):
        print("wallahhh you won the game habibi<<<<")
    
        break

    elif(num>=1 and num<=10):
        print("HINT: its between 1 to 10")
        print("you lost one more chance")

    elif(num>10 and num<=20):
        print("HINT: its between 10 to 20")
        print("you lost one more score")

    elif(num>20 and num<=30):
        print("HINT: its between 20 to 30")
        print("you lost one more score")
    
# if guessing exceeds more than limit
# give following output
else:
    print("the number is ", num)
    print("maybe better luck next time habibi>>>")
    
    

