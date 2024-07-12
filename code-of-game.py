                                     # Snake, Water, Gun game 

import random
# random module is used to select the value in between the range. 

print("Following are the options:- ")
print("Snake \nWater \nGun")

# dictonary for the key vlaue pair of snake , water and gun
dic = {1: "snake", 2 : "water", 3 : "gun"}
yrchoice = input("Enter your choice: ").lower()

# random.randrange(start,end)
computer = random.choice([1,2,3])
comp = dic[computer]

if(yrchoice == comp):
    print(f"Your choice {yrchoice}, Opponent choice {comp} -Game Draw")
elif(yrchoice == "snake" and comp =="gun"):
    print("Your choice",yrchoice,"opponent choice", comp,": Opponnet win")
elif(yrchoice =="snake"and comp =="water" ):
    print("Your choice",yrchoice,"opponent choice", comp,": You win")
elif(yrchoice =="water"and comp == "snake"):
    print("Your choice",yrchoice,"opponent choice", comp,": Opponnet win")
elif(yrchoice =="water" and comp == "snake"):
    print("Your choice",yrchoice,"opponent choice", comp,": Opponnet win")
elif(yrchoice == "water"and comp == "gun"):
    print("Your choice",yrchoice,"opponent choice", comp,": You win")
elif(yrchoice =="gun" and comp == "snake"):
    print("Your choice",yrchoice,"opponent choice", comp,": You win")
elif(yrchoice == "gun" and comp =="water" ):
    print("Your choice",yrchoice,"opponent choice", comp,": Opponnet win")
else:
    print("Your choice",yrchoice,"opponent choice", comp,": Something Went wrong !!")
