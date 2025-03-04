import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])#will pick a random integer out of these 3
youStr = input("Enter your choice: ")#enter a character
youDict = {"s": 1, "w": -1, "g": 0}#each character has a key
reverseDict = {1: "Snake", -1 : "Water", 0: "Gun"}#they key gets reversed into its element
you = youDict[youStr]#this will store they key i.e the integer

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Draw")
    
else: 
    if(computer == -1 and you ==-1):
        print("You win")
    
    elif(computer == -1 and you ==0):
        print("You lose")

    elif(computer == 1 and you ==-1):
        print("You lose")
        
    elif(computer == 1 and you == 0):
        print("You win")

    elif(computer == 0 and you ==-1):
        print("You win")
        
    elif(computer == 0 and you ==1):
        print("You lose")
        
    else:
        print("Something is wrong")
