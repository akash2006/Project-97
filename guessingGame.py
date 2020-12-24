import random

userNum = int(input("Guess a number between 0 to 9\n"))
randomrange = [0,1,2,3,4,5,6,7,8,9]
randomNum = round(random.randint(0,9))
tries=0
while True:
    if(tries==5):
        print("You ran out of tries :(")
        break
    if(userNum < randomNum & tries<5):
        tries=tries+1
        userNum=int(input("Your guess was lower than the answer. Try once more.\n"))
    elif(userNum > randomNum & tries < 5):
        tries=tries+1
        userNum=int(input("Your guess was higher than the answer. Try once more.\n"))
    elif(userNum==randomNum):
        print("Yay!!! You made it. That's the correct guess and you guessed that in ",tries," tries. Corret answer:",randomNum)
        break
    
        