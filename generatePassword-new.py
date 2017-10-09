import random
import time
import csv
import sys

sys.argv

numberOfWords = int(sys.argv[1])

#numberOfWords = int(numberOfWords)

currentTime = int(time.time())
randomInt = random.randint(1,1000000)

myHash = currentTime * randomInt

random.seed(myHash)
finalPassphrase = ""

for z in range(numberOfWords):
	finalCode = ""
	finalCode = str(finalCode)
	
	for x in range(5):
		anInt = random.randint(1,6)
		anInt = str(anInt)
		finalCode = finalCode + anInt

    print("Final Code: " + finalCode)
   
	with open('dicewareList.csv') as csvfile:
		reader = csv.DictReader(csvfile)
    	for row in reader:
			idNumber = int(row["idNumber"])
			associatedWord = str(row["associatedWord"])
			if int(finalCode) == idNumber:
				newWord = associatedWord
    		
    		if z == 0:
				finalPassphrase = finalPassphrase + newWord
			else:
				finalPassphrase = finalPassphrase + " + " + newWord
			
print("Final Passphrase: " + finalPassphrase)


