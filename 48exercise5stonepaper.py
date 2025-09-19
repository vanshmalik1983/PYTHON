import random

def check(comp,user):
    if (comp == user):
        return 0 
    

    if(comp == 0 and user == 1):
        return -1
    
    if(comp == 1 and user == 2):
        return -1
    
    if(comp == 2 and user == 0):
        return -1
    
    return 1 
   
    


comp = random.randint(0,2)
user = int(input(" 0 for stone, 1 for scissor and 2 for paper : \n "))

score = check(comp,user)

print("you: ",user)
print("comp: ",comp)

if(score == 0):
    print("Its draw")
elif(score ==1):
    print("You won")
else:
    print("You loose")
