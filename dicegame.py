import random

player_point=0;
Cpu_point=0;

print("GAME BEGINING")

while  (player_point!=10) and (Cpu_point!=10) :
 k=input("PRESS any key")
 player = random.randrange(1,6)
 cpu = random.randrange(1,6)
 print ("CPU is rolling dices ....")
 print("computer throws {:d}".format(cpu))
 print ("You re rolling dices ....")
 print("You throws {:d}".format(player))

 if player>cpu :
     player_point += 1
     print("YOU: {:d}  -------- CPU: {:d}".format(player_point,Cpu_point))
 elif cpu > player:
    Cpu_point += 1
    print("YOU: {:d}  -------- CPU: {:d}".format(player_point,Cpu_point))
 else:
    print ("DRAW!")
     print("YOU: {:d}  -------- CPU: {:d}".format(player_point,Cpu_point))

 
