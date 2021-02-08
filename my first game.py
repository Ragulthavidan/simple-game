import random
luckynum=random.randint(1,10)

choice=0
while choice<5:
    userchoice = int(input("guess my lucky number"))
    if userchoice>luckynum:
        print("you entered largest number than lucky num")
    elif userchoice<luckynum:
        print("you entered smallest number")
    elif userchoice==luckynum:
         print("congrats")
         break
    choice+=1