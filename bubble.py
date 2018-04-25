from random import randrange
import numpy as np

from datetime import datetime
startTime = datetime.now()

x=np.random.randint(100, size=100)

for i in range(len(x)):
    print (str(x[i]), end=' ')
    for j in range(x[i]):
        print ("*", end=' ')


    print("")
        

print("---------------------------------------------------")


for i in range (len(x)):
    for j in range(i):
        if (x[i]>x[j]):
            temp=x[i]
            x[i]=x[j]
            x[j]=temp




print("---------------------------------------------------")



for i in range(len(x)):
    print (str(x[i]), end=' ')
    for j in range(x[i]):
        print ("*", end=' ')


    print("")
        


print(datetime.now() - startTime)
