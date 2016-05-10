import random
import time
import csv

currentTime = int(time.time())
randomInt = random.randint(1,1000000)

myHash = currentTime * randomInt

random.seed(myHash)

finalCode = ''
finalCode = str(finalCode)

for x in range(5):
    
    anInt = random.randint(1,6)
    anInt = str(anInt)
    finalCode = finalCode + anInt

print "Number: " + finalCode




with open('dicewareList.csv') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         print(', '.join(row))


