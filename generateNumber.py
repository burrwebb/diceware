import random
import time

currentTime = int(time.time())
randomInt = random.randint()

myHash = currentTime

random.seed(myHash)

finalCode = ''
finalCode = str(finalCode)

for x in range(5):
    
    anInt = random.randint(1,6),
    anInt = str(anInt)
    finalCode = finalCode + anInt

print finalCode