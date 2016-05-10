import random
import time
import csv


numberOfWords = 5

currentTime = int(time.time())
randomInt = random.randint(1,1000000)

myHash = currentTime * randomInt

random.seed(myHash)


finalCode = str(finalCode)


for z in range(numberOfWords):
    finalCode = ""
    finalCode = str(finalCode)
    
    for x in range(5):
        
        anInt = random.randint(1,6)
        anInt = str(anInt)
        finalCode = finalCode + anInt

    print ""
    print "Number: " + finalCode


    with open('dicewareList.csv') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
              idNumber = int(row["idNumber"])
              associatedWord = str(row["associatedWord"])
              if int(finalCode) == idNumber:
                  print "Word: " + associatedWord





#######################################################
# with open('dicewareList.csv') as csvfile:
#      reader = csv.DictReader(csvfile)
#      for row in reader:
#          idNumber = int(row["idNumber"])
#          associatedWord = str(row["associatedWord"])
#
#          print "The ID number is: " + str(idNumber) + " and the word is: " + associatedWord
#######################################################


