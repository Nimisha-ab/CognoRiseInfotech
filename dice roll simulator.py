import random
dice=int(input(" no of dice:"))

if(dice<=0):
    print("must have atleast one dice")
    quit()

sides=int(input("no of sides:"))

if(sides<=0):
    print("must have atleast one side")
    quit()

roll=[]

for i in range(0,dice):
    face=random.randint(1,sides)
    roll.append(face)

print(roll)